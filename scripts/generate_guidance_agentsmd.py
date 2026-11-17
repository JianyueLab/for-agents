# -*- coding: utf-8 -*-
"""根据指导文件的开头说明生成索引"""

import argparse
import sys
from pathlib import Path
from urllib.parse import quote


GUIDANCE_DIRECTORY = Path(__file__).resolve().parent.parent / "guidance"


def read_description(path: Path) -> str:
    """提取文件开头由分隔线包裹的说明"""
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"{path}: 文件必须以 --- 开始")

    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            description = "\n".join(lines[1:index]).strip()
            if not description:
                raise ValueError(f"{path}: 开头说明不能为空")
            return description

    raise ValueError(f"{path}: 开头说明缺少结束分隔线 ---")


def generate_content() -> str:
    """按相对路径排序生成指导索引"""
    if not GUIDANCE_DIRECTORY.is_dir():
        raise ValueError(f"指导目录不存在: {GUIDANCE_DIRECTORY}")

    sections = [
        "# 指导文件索引",
        "根据下面的适用场景 按需阅读对应的指导文件",
    ]
    for path in sorted(GUIDANCE_DIRECTORY.rglob("*.md")):
        if path.name == "AGENTS.md" or not path.is_file():
            continue
        relative_path = path.relative_to(GUIDANCE_DIRECTORY).as_posix()
        description = read_description(path)
        link = quote(relative_path, safe="/")
        label = relative_path.replace("[", "\\[").replace("]", "\\]")
        sections.append(f"## [{label}](./{link})\n\n{description}")

    return "\n\n".join(sections) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="检查索引是否最新 不写入文件"
    )
    args = parser.parse_args()
    output_path = GUIDANCE_DIRECTORY / "AGENTS.md"

    try:
        content = generate_content()
        current_content = (
            output_path.read_text(encoding="utf-8") if output_path.exists() else None
        )
        if args.check:
            if current_content != content:
                print("指导索引需要更新 请运行 task generate:guidance", file=sys.stderr)
                return 1
            print("指导索引已是最新")
        elif current_content == content:
            print("指导索引无变化")
        else:
            with output_path.open("w", encoding="utf-8", newline="\n") as output:
                output.write(content)
            print(f"已生成 {output_path}")
    except (OSError, UnicodeError, ValueError) as error:
        print(f"生成指导索引失败: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
