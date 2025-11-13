# Tools and Automation - Reference Guide

## Export & Publishing

### obsidian-export (Rust CLI)
Convert vault to standard markdown
```bash
cargo install obsidian-export
obsidian-export /path/to/vault /path/to/output/
```
**GitHub**: https://github.com/zoni/obsidian-export

### Quartz v4
Static site generator for Obsidian
**Features**: Wikilinks, backlinks, graph, search
**GitHub**: https://github.com/jackyzha0/quartz
**Docs**: https://quartz.jzhao.xyz

### Obsidian Digital Garden
Netlify publishing plugin
**Control**: `dg-publish: true` in frontmatter
**GitHub**: https://github.com/oleeskild/obsidian-digital-garden

## Terminal Access

### obsidian-cli (Yakitrak)
CLI for vault operations
```bash
# Mac/Linux
brew tap yakitrak/yakitrak
brew install yakitrak/yakitrak/obsidian-cli

# Commands
obsidian-cli open [note]
obsidian-cli daily
obsidian-cli search [query]
obsidian-cli create [note]
```
**GitHub**: https://github.com/Yakitrak/obsidian-cli

## Programmatic Access

### Local REST API Plugin
REST API for external automation
**Install**: Community Plugins → "Local REST API"
**Capabilities**: CRUD operations, run commands, manage metadata
**Docs**: https://coddingtonbear.github.io/obsidian-local-rest-api/

### MCP Servers (Claude Code Integration)
```bash
npx -y @smithery/cli install mcp-obsidian --client claude
```
**Operations**: Read, search, update, frontmatter, tags
**GitHub**: https://github.com/smithery-ai/mcp-obsidian

## Batch Metadata Management

### obsidian-metadata (Python)
Bulk metadata operations
```bash
pip install obsidian-metadata
```
**Workflow**: Export CSV → Edit → Import → Commit
**GitHub**: https://github.com/natelandau/obsidian-metadata

## Sync & Backup

### Obsidian Git
Version control for vault
**Features**: Auto-commit, source control view, diff view
**Note**: Limited mobile support
**GitHub**: https://github.com/Vinzent03/obsidian-git

### Remotely Save
Multi-cloud sync
**Supports**: S3, Dropbox, OneDrive, WebDAV, Google Drive
**Features**: Encryption, conflict resolution, mobile-friendly
**GitHub**: https://github.com/remotely-save/remotely-save

## Automation Plugins

### Templater
Advanced templates with JavaScript
**Capabilities**: Variables, functions, system commands
**Security**: Can execute code - trust required
**GitHub**: https://github.com/SilentVoid13/Templater

### QuickAdd
Macro automation system
**Features**: Chain operations, custom scripts
**Docs**: https://quickadd.obsidian.guide
**GitHub**: https://github.com/chhoumann/quickadd

### Linter
Automated formatting
**Triggers**: On save or manual
**Rules**: Frontmatter, headings, spacing, content
**GitHub**: https://github.com/platers/obsidian-linter

### Advanced URI
Deep linking and automation
**Examples**:
```
obsidian://adv-uri?vault=<vault>&daily=true
obsidian://adv-uri?vault=<vault>&filepath=<file>&commandid=<cmd>
```
**Use**: iOS Shortcuts, external automation
**GitHub**: https://github.com/Vinzent03/obsidian-advanced-uri

## Python/JavaScript Libraries

### obsidiantools (Python)
Vault analytics and network analysis
```bash
pip install obsidiantools
```
**Features**: NetworkX graphs, broken links, orphaned notes
**GitHub**: https://github.com/mfarragher/obsidiantools

### obsidian-vault-parser (npm)
Parse vault structure
```bash
npm i obsidian-vault-parser
```
**GitHub**: https://www.npmjs.com/package/obsidian-vault-parser

## Quick Reference by Use Case

**Export**: obsidian-export
**Terminal**: obsidian-cli (Yakitrak)
**Automation**: Local REST API + MCP
**Metadata**: obsidian-metadata (Python)
**Publishing**: Quartz or Digital Garden
**Sync**: Obsidian Git (desktop), Remotely Save (mobile)
**Formatting**: Linter plugin
**Analytics**: obsidiantools (Python)

## Resources

- **Community Plugins**: https://obsidian.md/plugins
- **GitHub Topics**: https://github.com/topics/obsidian
- **Plugin Stats**: https://www.obsidianstats.com