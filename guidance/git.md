---
当你需要操作 Git 时，请参考此说明
对于 `.gitignore` 以及 `.gitattributes` 的编写，也请参考此说明
---

本项目全部使用 Git 作为主要的版本控制系统（VCS），每个子项目都应该是一个 Git 仓库（Git Repository）

主分支使用 `main` 而不是 `master`

## 工作流

项目使用 Rebase 与 Squash 工作流，不使用 Merge

## Commit Message

Git 提交消息的格式有非常严格的规定，这些规定是在 Conventional Commits 上建立的

### 通用规则

- 尽可能将 `header` 行的长度限制在 70 个字符以内 
- 不要以句号结尾
- 非格式要求的地方不使用标点符号，逗号使用空格替代
- 每个提交都应该只包含一个稳定的变更
- 对于中文中出现了英文的地方，在英文两侧加上一个空格

### 提交信息格式

每个提交信息包含三个部分：`header`、可选的 `body` 和 `footer`

其中头部具有特殊的格式，其中包括 `type`、可选的 `scope` 和 `description`

`BLANK LINE` 为空行

```text
<type>(<optional scope>): <description>
<BLANK LINE>
<optional body>
<BLANK LINE>
<optional footer>
```

#### type

type 必须是以下几种类型之一：

| 类型          | 说明                                                         |
|---------------|--------------------------------------------------------------|
| **build:**    | 影响构建系统或外部依赖的变更，例如 python、pnpm              |
| **ci:**       | 修改 CI 配置文件和脚本                                       |
| **docs:**     | 仅涉及文档的变更                                             |
| **feat:**     | 新增功能                                                     |
| **fix:**      | 修复 Bug                                                     |
| **perf:**     | 优化性能的代码变更                                           |
| **refactor:** | 重构代码，既不修复 Bug，也不新增功能                         |
| **chore:**    | 不影响功能的必要维护性变更，例如更新依赖、添加监控埋点等     |
| **style:**    | 不影响代码含义的格式变更，例如空白字符、代码格式、缺失分号等 |
| **test:**     | 添加缺失的测试或修正现有测试                                 |
| **meta:**     | 修改仓库元信息，例如所有者配置文件、编辑器配置等             |
| **license:**  | 修改许可证相关内容                                           |

#### scope

`scope` 应该是指受影响的核心组件的名称

这意味着该范围应该涵盖整个系统，而不仅仅是被修改的文件本身

例如，如果代码主要影响计费功能，那么就应该使用 `billing` 作为 `scope`，即使这些变更发生在工具文件或数据库 schema 中

你应当阅读项目的历史提交信息，统一相同 `scope` 的名称

`scope` 不是必要的，当涉及多个复杂的部分或你认为可以省略 `scope` 的时候，可以省去不写

`scope` 部分使用英文编写

#### description

`description` 部分是对本次提交的概括性的简短描述，尽可能在一个短句内完成

主要使用中文，但该写英文的就写英文，不要强硬的翻译

对于中文中出现了英文的地方，在英文两侧加上一个空格

结尾不加句号，逗号使用空格替代

#### body

`body` 部分是你在认为有必要的时候对本次提交作出的更详细描述

语言和标点要求同 `description` 部分

#### footer

`footer` 部分用于在需要的时候扩展本次提交的作用，如关闭 Issue、关联 PR、跳过 CI 等

| **语法**           | **作用**                 | **示例**                        |
|--------------------|--------------------------|---------------------------------|
| `Resolves #123`    | 解决并关闭关联的 Issue   | `Resolves #123`                 |
| `Refs #123`        | 关联 Issue，但不自动关闭 | `Refs #123`                     |
| `Related to #123`  | 声明相关 Issue           | `Related to #123`               |
| `See PR #123`      | 引用关联的 PR            | `See PR #123`                   |
| `Co-authored-by:`  | 声明共同作者             | `Co-authored-by: Name <email>`  |
| `Signed-off-by:`   | 添加签署者信息           | `Signed-off-by: Name <email>`   |
| `BREAKING CHANGE:` | 声明不兼容变更及其影响   | `BREAKING CHANGE: ...`          |
| `[skip ci]`        | 请求 CI 跳过本次提交     | `docs: update README [skip ci]` |

## Branch

一个 git 仓库只能有一个主分支、一个开发分支以及一个部署分支，可以有多个功能分支

- 主分支使用 `main`，是项目稳定代码，合并自 `dev` 分支
- 开发分支使用 `dev`，是项目最新的开发代码，合并自其他功能分支
- 部署分支使用 `deploy`，是项目线上正在运行的版本代码，合并自 `main` 分支

### 功能分支

使用格式 `<type>/<short-description>` :

- type: 应为 `feat` `fix` `ref` `perf` `docs` `test` `ci` `build` `chore` `style` `meta` `license` 中的一个
- short-description: 这种改变是关于什么的，使用 kebab 格式表达

## Pull Request

不同的分支应当使用 PR 进行合并，并确保必要的检查通过（极特殊情况除外）

PR 的标题编写格式要求与 Commit Message 的 `header` 一致

另外，使用 `[WIP] ` （注意后面有个空格）作为标题开头的的 PR 代表正在进行中的工作，不应该进行合并操作

如果本次 PR 中的 commit 繁多且复杂，考虑使用 Squash，然后重新编写一个清晰的 message 表示本次 PR 的整体更改

## .gitignore 文件

`.gitignore` 文件至少包括以下部分

- 常见操作系统（macOS、Linux、Windows）的特殊文件
- 对 IDE 多余文件的排除，应当被包含的配置文件除外，`/.idea` 整个排除
- 常见的日志与缓存文件
- 敏感信息以及生产配置文件
- 语言和工具链应当排除的内容
- 应当排除的中间产物
- `CLAUDE.md`

## .gitattributes 文件

- 优先使用 `text=auto`
- 不要随意设置 binary
