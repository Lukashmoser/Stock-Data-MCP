# Session rules

You are in a fresh session, as if the user had just opened a new chat and sent you one message. You know nothing about any earlier work.

**The user's message** is the full content of the prompt file named in your task (in /home/claude/results/2026-10-13/prompts/). Read it and respond exactly as if the user had typed it.
- If it starts with a slash command such as `/earnings`, the user is invoking a plugin skill. Load it with the Skill tool under the matching name: `equity-research:<command>` or `financial-analysis:<command>`.
- If it names a skill ("Use the deck-refresh skill"), load that skill with the Skill tool (for example `financial-analysis:deck-refresh`).
- Any file in your run folder (other than your own outputs) is an attachment the user sent with the message.

**Files**
- Read only your run folder, the prompt file(s) named in your task, and this rules file.
- Don't open anything else under /home/claude/results, /mnt/user-data, /tmp, /root or ~/.claude.
- Save every deliverable to your run folder.
- Put all scratch files and build scripts in a `_work/` subfolder of your run folder. Never use /tmp or the shared scratchpad: other sessions run alongside you and write there.

**The user can't answer questions during this run.** Don't use AskUserQuestion. Treat these as the user's replies:
- To any confirmation or clarifying question: "Proceed with your recommended defaults and don't stop for further confirmation. List the assumptions you made under "Estimates and gaps" in the Comparison Block."
- To an approval gate for a deck refresh: "Approved. Apply every change in the plan, including the flagged derived numbers."
- If your reply would end without a Comparison Block: "Please add the Comparison Block now, exactly as specified at the end of my first message." So always include it.

Use whatever tools and data sources you would normally use, with one exception: the stock-data tools are switched off in this session. Do not load or call any tool whose name contains "stock-data". If a skill mentions them, treat them as unavailable.

**When you finish**, write `transcript.md` in your run folder with:
1. Start and end time. Run `date -u` at the very start and at the end.
2. Your full final reply to the user, ending with the Comparison Block.
3. A section `## Run log` listing every tool you called with call counts, including ToolSearch queries and skills loaded, plus the files you delivered.

Your final message back should contain only the Comparison Block and the Run log.
