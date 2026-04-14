# LaTeXmk 配置文件 - Elsarticle 模板配置
# 使用 pdfLaTeX 编译
$pdf_mode = 1;
$pdflatex = "pdflatex -file-line-error -synctex=1 -interaction=nonstopmode %O %S";

# 启用 BibTeX 编译（用于 elsarticle 参考文献）
$bibtex_use = 2;  # 强制每次运行BibTeX

# 自动清理辅助文件（包含 BibTeX 相关文件）
$clean_ext = "bbl blg run.xml spl";

# 生成的PDF预览器（macOS）
$pdf_previewer = "open -a Preview %S";

# 注意：不要启用 $preview_continuous_mode = 1，
# VS Code LaTeX Workshop 的 onSave 已处理自动重编译。
