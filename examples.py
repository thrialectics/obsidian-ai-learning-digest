"""Few-shot examples for the summarizer."""

FEW_SHOT_EXAMPLES = """
Example 1:

Input notes:
## llm-training-techniques.md
RLHF is becoming standard for aligning LLMs with human preferences. Started with InstructGPT, now used in Claude, GPT-4, etc. Key challenge is creating diverse, high-quality feedback data. Constitutional AI is an alternative that uses AI feedback instead of human labelers.

## vector-database-comparison.md
Compared Pinecone, Weaviate, and Milvus for my RAG application. Pinecone has simple API but higher cost. Weaviate offers hybrid search capabilities. Milvus scales better for my expected data volume. Going with Milvus for now.

Example summary:
Today's notes covered two AI infrastructure topics: (1) LLM training techniques focusing on RLHF as the standard alignment method and Constitutional AI as an emerging alternative; (2) A comparison of vector databases (Pinecone, Weaviate, and Milvus) for RAG applications, with Milvus selected for its superior scaling capabilities.

Example glossary:
* RLHF (Reinforcement Learning from Human Feedback) - A technique to align LLMs with human preferences using human evaluations of model outputs
* Constitutional AI - An alignment approach that uses AI feedback instead of human labelers to train models according to constitutional principles
* RAG (Retrieval-Augmented Generation) - A technique that enhances LLM outputs by retrieving relevant context from external knowledge sources
* Vector Database - Specialized database optimized for storing and querying vector embeddings
* Pinecone - A managed vector database service with simple API but higher costs
* Weaviate - A vector database with hybrid search capabilities combining vector and keyword search
* Milvus - An open-source vector database with strong scaling capabilities for large data volumes

Example 2:

Input notes:
## autonomous-agent-architecture.md
Designed a multi-agent system using ReAct framework. Agents maintain working memory, use tools including web search and code execution. Planning agent coordinates 3 specialist agents. Communication through structured JSON. Need to implement better conflict resolution.

## zero-day-vulnerabilities-research.md
Read about recent zero-day in Chrome's V8 engine. Attackers using type confusion to achieve remote code execution. Defense-in-depth strategies essential: sandboxing, privilege separation, ASLR. Added Synk scanning to our CI/CD pipeline for early detection.

## solo-dev-productivity.md
Time-blocking technique working well for deep work. 90-minute blocks with no distractions. Using Pomodoro (25/5) for administrative tasks. Weekly review crucial for course correction. Need to improve estimation - consistently underestimating tasks by ~30%.

Example summary:
Today's notes covered three areas: (1) Architectural design for an autonomous multi-agent system using the ReAct framework with specialized agents communicating via JSON; (2) Research on zero-day vulnerabilities, specifically in Chrome's V8 engine, and implemented defense strategies including Synk scanning in CI/CD; (3) Productivity techniques for solo development including time-blocking, Pomodoro for admin tasks, and weekly reviews, with a note about estimation challenges.

Example glossary:
* ReAct (Reasoning + Acting) - A framework enabling LLM agents to combine reasoning with action-taking in interactive environments
* Multi-agent system - A system where multiple AI agents collaborate to solve problems, often with specialized roles
* Working memory - A temporary storage and manipulation space for information an agent is currently processing
* Zero-day vulnerability - A software security flaw unknown to the vendor that hackers can exploit before it's patched
* Type confusion - A memory vulnerability where a program accesses memory using an incompatible type
* Defense-in-depth - A cybersecurity approach using multiple protective mechanisms rather than a single strong barrier
* ASLR (Address Space Layout Randomization) - A security technique that randomizes memory addresses to prevent exploitation
* CI/CD pipeline - Continuous Integration/Continuous Deployment automation for software delivery
* Time-blocking - A productivity technique allocating specific time periods for focused work on particular tasks
* Pomodoro Technique - A time management method using 25-minute focused work periods separated by short breaks
""" 