import gradio as gr

def show_note(note):
    return f"这段笔记有 {len(note)} 个字符。\n\n原文：\n{note}"

gr.Interface(
    fn=show_note,
    inputs=gr.Textbox(label="输入笔记", lines=5),
    outputs=gr.Textbox(label="显示结果", lines=5),
    title="我的第一个笔记小工具",
).launch(inbrowser=True, share=False)