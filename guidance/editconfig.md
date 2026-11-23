---
当你需要编写 `.editconfig` 文件时，请参考此说明
---

## editconfig 文件

使用 `.editconfig` 作为文件名

一般来说，填写以下内容即可

```editorconfig
root = true

[*]
charset = utf-8
end_of_line = lf
indent_size = 4
indent_style = space
insert_final_newline = true
max_line_length = 120
tab_width = 4
trim_trailing_whitespace = true

[*.{yml,yaml,json,html,htm,xml,svg,css,scss,less}]
indent_size = 2
tab_width = 2

```

在一些特殊情况下，你可以灵活增加和修改项目

## 修改后的提交

当你在原有基础上修改 `.editconfig` 文件后，请独立提交并使用 `meta: editconfig` 作为 commit message
