#!/usr/bin/env python3
"""墨匣网文质量检查：字数统计 + AI 高频词检测"""

import sys
import re
from pathlib import Path


def count_chinese_chars(text: str) -> int:
    """统计中文字符数（不含标点和空白）"""
    return len(re.findall(r'[\u4e00-\u9fff]', text))


def check_ai_patterns(text: str) -> dict:
    """检测 AI 高频词"""
    patterns = {
        '仿佛': r'仿佛',
        '好像': r'好像',
        '似乎': r'似乎',
        '宛如': r'宛如',
        '犹如': r'犹如',
    }
    results = {}
    for word, pattern in patterns.items():
        count = len(re.findall(pattern, text))
        results[word] = count
    return results


def check_degeneration(text: str) -> list:
    """检测退化问题：复读、截断、工程词泄漏"""
    issues = []
    # 连续重复句子
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i in range(len(lines) - 1):
        if lines[i] == lines[i + 1]:
            issues.append(f'复读：第{i+1}行与第{i+2}行完全相同')
    # 工程词泄漏
    leak_words = ['作为一个', '总而言之', '综上所述', '首先', '其次', '最后']
    for word in leak_words:
        if word in text:
            issues.append(f'工程词泄漏：包含"{word}"')
    return issues


def main():
    if len(sys.argv) < 2:
        print('用法: python check_wordcount.py <正文文件>')
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f'文件不存在: {file_path}')
        sys.exit(1)

    text = file_path.read_text(encoding='utf-8')

    # 字数统计
    char_count = count_chinese_chars(text)
    print(f'中文字数: {char_count}')
    if char_count < 8000:
        print(f'⚠ 字数不足，目标 8000-15000，当前 {char_count}')
    elif char_count > 15000:
        print(f'⚠ 字数超标，目标 8000-15000，当前 {char_count}')
    else:
        print('✓ 字数达标')

    # AI 高频词
    print('\n--- AI 高频词检测 ---')
    ai_patterns = check_ai_patterns(text)
    total_ai = sum(ai_patterns.values())
    for word, count in ai_patterns.items():
        if count > 0:
            print(f'  {word}: {count} 处')
    if total_ai > 10:
        print(f'⚠ AI 高频词共 {total_ai} 处，超过 10 处阈值，建议复核')
    else:
        print(f'✓ AI 高频词共 {total_ai} 处，在阈值内')

    # 退化检测
    print('\n--- 退化检测 ---')
    issues = check_degeneration(text)
    if issues:
        for issue in issues:
            print(f'  ⚠ {issue}')
    else:
        print('✓ 未发现退化问题')


if __name__ == '__main__':
    main()
