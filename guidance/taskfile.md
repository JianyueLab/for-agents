---
当你需要为项目配置 Taskfile、定义任务、编写自动化时，请参考此说明
---

项目使用 [taskfile](https://taskfile.dev/) 进行工作，如果本地发现没有安装 `task` 命令，请明确提示开发者是否进行安装

每个项目都需要使用 taskfile 进行管理，即使已经在有语言工具链的情况下，Taskfile 是命令运行的唯一入口，但在调试情况下除外

## taskfile 文件

taskfile 统一使用 `taskfile.yaml` 作为文件名，放置在项目根目录下

若有子任务需要拆分文件，请放置在根目录下的 `.task` 文件夹中，文件名为子任务的名字，后缀统一使用 `yaml`，并在根目录中的
`taskfile.yaml` 中引用。

## taskfile 的编写规范

参考[taskfile/schema文档](https://taskfile.dev/docs/reference/schema)中的说明，灵活编写 taskfile 中的内容

### task

在所有主 taskfile 中编写以下 tasks，以在没有输入的时候打印所有可运行的 task

```yaml
default:
  cmds:
    - task --list
  silent: true
```

下面的 task 不是必要的，但当你需要编写对应功能的时候，请参考以下名称

*`xxx`为可选的占位部分*

- bootstrap 项目初始化与开发环境准备
- lint[:xxx] 用于对项目代码的完整或部分代码质量检查
- check[:xxx] 用于对项目的完成或部分综合正确性检查
- format 代码格式化
- build[:xxx] 构建
- test[:xxx] 运行全部或部分测试
- generate[:xxx] 代码生成
- clean 清理构建产物与临时文件
- devenv[:xxx] 本地开发环境管理
- migrate[:xxx] 执行数据或配置迁移
- sync[:xxx] 同步资源、配置或依赖
- package 打包

### task 编写

每个 `task` 都需要带上 `desc` 用于描述这个任务的功能，使用一个短句，使用双引号包裹，`default` 除外
