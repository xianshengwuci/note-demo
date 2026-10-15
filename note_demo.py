import gradio as gr


def organize_note(note):
    groups = {
        "已完成": [],
        "待确认": [],
        "下一步": [],
        "未分类": [],
    }

    rules = {
        "已完成": ("已完成：", "完成："),
        "待确认": ("待确认：", "疑问："),
        "下一步": ("下一步：", "待办："),
    }

    for line in note.splitlines():
        text = line.strip()
        if not text:
            continue

        matched = False

        for category, prefixes in rules.items():
            for prefix in prefixes:
                if text.startswith(prefix):
                    groups[category].append(text[len(prefix):].strip())
                    matched = True
                    break
            if matched:
                break

        if not matched:
            groups["未分类"].append(text)

    result = []
    for category, items in groups.items():
        if items:
            content = "\n".join(f"- {item}" for item in items)
        else:
            content = "- （暂无）"

        result.append(f"{category}\n{content}")

    return "\n\n".join(result)


gr.Interface(
    fn=organize_note,
    inputs=gr.Textbox(label="输入笔记（每条一行）", lines=8),
    outputs=gr.Textbox(label="整理结果", lines=12),
    title="我的笔记分类小工具",
    description="用“已完成：”“待确认：”“下一步：”作为每条笔记的开头。",
).launch(inbrowser=True, share=False)
