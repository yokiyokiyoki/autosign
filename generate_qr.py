# /// script
# dependencies = [
#   "qrcode[pil]",
# ]
# ///
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from tkinter import Tk, messagebox, simpledialog
from urllib.parse import urlparse

import qrcode


def is_valid_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def build_output_path() -> Path:
    desktop = Path.home() / "Desktop"
    output_dir = desktop if desktop.exists() else Path.cwd()
    filename = f"qrcode_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    return output_dir / filename


def open_image(path: Path) -> None:
    if sys.platform.startswith("win"):
        os.startfile(path)  # type: ignore[attr-defined]
        return

    command = ["open", str(path)] if sys.platform == "darwin" else ["xdg-open", str(path)]
    subprocess.Popen(command)


def generate_qr(url: str, output_path: Path) -> None:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)


def main() -> None:
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    try:
        url = simpledialog.askstring(
            "二维码生成",
            "请输入要生成二维码的 URL（必须包含 http:// 或 https://）",
            parent=root,
        )
        if url is None:
            return

        normalized_url = url.strip()
        if not normalized_url:
            messagebox.showerror("输入错误", "URL 不能为空。", parent=root)
            return

        if not is_valid_url(normalized_url):
            messagebox.showerror(
                "输入错误",
                "URL 格式不正确，请输入以 http:// 或 https:// 开头的完整链接。",
                parent=root,
            )
            return

        output_path = build_output_path()
        generate_qr(normalized_url, output_path)
        messagebox.showinfo("生成成功", f"二维码已生成：\n{output_path}", parent=root)
        open_image(output_path)
    except Exception as error:
        messagebox.showerror("生成失败", f"处理失败：{error}", parent=root)
    finally:
        root.destroy()


if __name__ == "__main__":
    main()
