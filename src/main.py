#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project_AIVideoFlow - 主程序
基于ComfyUI的全自动多模态AI视频生产流
"""

import os
import sys
import argparse
import logging
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.data_acquisition import WebScraper
from src.image_processor import ImageProcessor
from src.prompt_engine import PromptEngine
from src.comfyui_client import ComfyUIClient

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('aivideoflow.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class AIVideoFlow:
    def __init__(self, config_path=None):
        """初始化AI视频生产流"""
        self.project_root = project_root
        self.config = self.load_config(config_path)
        
        # 初始化组件
        self.scraper = WebScraper(self.config)
        self.image_processor = ImageProcessor(self.config)
        self.prompt_engine = PromptEngine(self.config)
        self.comfyui_client = ComfyUIClient(self.config)
        
        logger.info("AI视频生产流初始化完成")
    
    def load_config(self, config_path):
        """加载配置文件"""
        import yaml
        
        if config_path is None:
            config_path = project_root / "config" / "config.yaml"
        
        if not Path(config_path).exists():
            logger.warning(f"配置文件不存在: {config_path}，使用默认配置")
            return self.get_default_config()
        
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            logger.info(f"配置文件加载成功: {config_path}")
            return config
        except Exception as e:
            logger.error(f"配置文件加载失败: {e}")
            return self.get_default_config()
    
    def get_default_config(self):
        """获取默认配置"""
        return {
            'web_scraping': {
                'target_url': None,
                'screenshot_dir': 'data/screenshots',
                'text_dir': 'data/texts'
            },
            'image_processing': {
                'output_dir': 'data/processed',
                'crop_region': [0, 0, 512, 512]  # x1, y1, x2, y2
            },
            'prompt_engineering': {
                'llm_provider': 'openai',
                'llm_model': 'gpt-4',
                'prompt_template': 'default'
            },
            'comfyui': {
                'server_url': 'http://localhost:8188',
                'workflow_file': '_Workflow_Files/video_star4.json',
                'output_dir': 'output/videos'
            }
        }
    
    def run_pipeline(self, target_url=None):
        """运行完整的工作流管道"""
        logger.info("开始运行AI视频生产流")
        
        try:
            # 步骤1: 数据采集
            logger.info("步骤1: 数据采集")
            screenshots, texts = self.scraper.capture_materials(target_url)
            
            if not screenshots:
                logger.error("未获取到截图，流程终止")
                return False
            
            # 步骤2: 图像处理
            logger.info("步骤2: 图像处理")
            processed_images = []
            for screenshot in screenshots:
                processed = self.image_processor.process_image(screenshot)
                if processed:
                    processed_images.append(processed)
            
            if not processed_images:
                logger.error("图像处理失败，流程终止")
                return False
            
            # 步骤3: 提示词工程
            logger.info("步骤3: 提示词工程")
            prompts = []
            for text in texts:
                prompt = self.prompt_engine.generate_prompt(text)
                if prompt:
                    prompts.append(prompt)
            
            if not prompts:
                logger.warning("提示词生成失败，使用默认提示词")
                prompts = ["high-quality anime style, cinematic lighting, detailed"]
            
            # 步骤4: 视频生成
            logger.info("步骤4: 视频生成")
            generated_videos = []
            
            for i, (image, prompt) in enumerate(zip(processed_images, prompts)):
                logger.info(f"生成视频 {i+1}/{len(processed_images)}")
                
                video_path = self.comfyui_client.generate_video(
                    image_path=image,
                    prompt=prompt,
                    output_name=f"video_{i+1}"
                )
                
                if video_path:
                    generated_videos.append(video_path)
                    logger.info(f"视频生成成功: {video_path}")
                else:
                    logger.error(f"视频生成失败: {image}")
            
            # 生成报告
            self.generate_report(screenshots, processed_images, prompts, generated_videos)
            
            logger.info(f"AI视频生产流完成，生成 {len(generated_videos)} 个视频")
            return True
            
        except Exception as e:
            logger.error(f"工作流执行失败: {e}", exc_info=True)
            return False
    
    def generate_report(self, screenshots, processed_images, prompts, videos):
        """生成执行报告"""
        report_dir = project_root / "reports"
        report_dir.mkdir(exist_ok=True)
        
        report_file = report_dir / f"execution_report_{time.strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write("AI视频生产流执行报告\n")
            f.write("=" * 60 + "\n\n")
            
            f.write(f"报告生成时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"原始截图数量: {len(screenshots)}\n")
            f.write(f"处理图像数量: {len(processed_images)}\n")
            f.write(f"生成提示词数量: {len(prompts)}\n")
            f.write(f"生成视频数量: {len(videos)}\n\n")
            
            f.write("处理详情:\n")
            f.write("-" * 60 + "\n")
            
            for i, (screenshot, processed, prompt, video) in enumerate(
                zip(screenshots, processed_images, prompts, videos), 1
            ):
                f.write(f"\n项目 {i}:\n")
                f.write(f"  原始截图: {Path(screenshot).name}\n")
                f.write(f"  处理图像: {Path(processed).name}\n")
                f.write(f"  提示词: {prompt[:100]}...\n")
                f.write(f"  生成视频: {Path(video).name}\n")
        
        logger.info(f"执行报告已生成: {report_file}")

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='AI视频生产流')
    parser.add_argument('--url', type=str, help='目标网址')
    parser.add_argument('--config', type=str, default=None, help='配置文件路径')
    parser.add_argument('--output', type=str, default='output', help='输出目录')
    parser.add_argument('--debug', action='store_true', help='调试模式')
    
    args = parser.parse_args()
    
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # 创建输出目录
    output_dir = Path(args.output)
    output_dir.mkdir(exist_ok=True)
    
    # 运行AI视频生产流
    pipeline = AIVideoFlow(config_path=args.config)
    
    if args.url:
        success = pipeline.run_pipeline(target_url=args.url)
    else:
        # 如果没有提供URL，使用配置文件中的URL
        success = pipeline.run_pipeline()
    
    if success:
        logger.info("AI视频生产流执行成功！")
        print("\n🎉 视频生成完成！")
        print(f"请查看 {output_dir} 目录中的输出文件")
    else:
        logger.error("AI视频生产流执行失败")
        print("\n❌ 视频生成失败，请查看日志文件了解详情")
    
    return 0 if success else 1

if __name__ == "__main__":
    import time
    sys.exit(main())