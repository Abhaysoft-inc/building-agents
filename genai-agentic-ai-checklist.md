# Gen AI & Agentic AI — Study Checklist
## Chapter-wise, topic-wise, theory + practical

Check items off as you complete them. Each topic = theory first, then a small isolated exercise before moving on.

---

## Chapter 0: Foundations *(already known — skip or skim)*
- [x] What an LLM actually is (next-token prediction, not "thinking")
- [x] Tokens, context windows, temperature
- [x] System vs user vs assistant roles
- [x] API basics — requests, responses, streaming

---

## Chapter 1: Prompt Engineering

### 1.1 Zero-Shot Prompting
- [ ] Theory: what zero-shot is, why it's the baseline, why output format/logic is unstable
- [ ] Practical: same task worded 3 ways, compare output stability

### 1.2 Few-Shot Prompting
- [ ] Theory: showing examples to fix a pattern, how many examples is "enough," example ordering effects
- [ ] Practical: sentiment/classification task — zero-shot vs few-shot side by side

### 1.3 Chain-of-Thought (CoT) Prompting
- [ ] Theory: why "think step by step" changes accuracy on reasoning tasks, when it helps vs when it's just noise
- [ ] Practical: a math/logic word problem — zero-shot vs CoT, compare correctness

### 1.4 Role / Persona Prompting
- [ ] Theory: how system prompts shape tone, expertise framing, and behavior boundaries
- [ ] Practical: same question answered as "terse expert" vs "patient teacher" persona

### 1.5 Structured Output (JSON mode / schema-constrained)
- [ ] Theory: why free text is unreliable for code to parse, schema enforcement, failure handling
- [ ] Practical: force JSON output, parse it in Python, deliberately break it to see failure mode

### 1.6 Prompt Iteration & Debugging
- [ ] Theory: how to diagnose *why* a prompt underperforms (ambiguity, missing constraints, wrong examples)
- [ ] Practical: take a bad prompt, iterate on it 3 times, log how output changes each round

**Chapter 1 Milestone:** Prompt comparison tool that tests any question across all 6 techniques.

---

## Chapter 2: Tool Use / Function Calling

### 2.1 The Tool-Calling Loop
- [ ] Theory: model requests a tool → you execute it in your code → you feed the result back to the model
- [ ] Practical: single tool (calculator), trace the full request → execute → respond cycle manually

### 2.2 Tool Schemas
- [ ] Theory: name/description/parameters — why the *description* matters as much as your prompt
- [ ] Practical: write 2 versions of the same tool's description (vague vs precise), compare how often the model calls it correctly

### 2.3 Multi-Tool Selection
- [ ] Theory: how the model decides *which* tool to use among several, ambiguity problems
- [ ] Practical: give it a search tool + calculator, ask mixed questions, observe selection accuracy

### 2.4 Handling Tool Errors
- [ ] Theory: what happens when a tool call fails, malformed arguments, retries
- [ ] Practical: deliberately break a tool (bad API key, bad input) and handle the failure gracefully

**Chapter 2 Milestone:** Assistant that can search the web and do math, choosing the right tool each time.

---

## Chapter 3: Agentic Loops (ReAct Pattern)

### 3.1 Reason → Act → Observe Loop
- [ ] Theory: the core loop that defines "agentic" — thinking, acting, observing results, deciding next step
- [ ] Practical: log every reasoning step to console for one multi-step task, watch it "think"

### 3.2 Multi-Step Planning
- [ ] Theory: breaking a broad goal into ordered sub-tasks, when planning helps vs adds overhead
- [ ] Practical: give it a genuinely multi-step goal (research X, compare Y, summarize) and trace its plan

### 3.3 Stopping Conditions
- [ ] Theory: how an agent decides it's "done," under- vs over-thinking
- [ ] Practical: add a max-iteration limit, observe what happens when the agent hits it

### 3.4 Common Failure Modes
- [ ] Theory: infinite loops, hallucinated tool calls, goal drift
- [ ] Practical: intentionally trigger a loop failure, then fix it with better stopping logic

**Chapter 3 Milestone:** First real autonomous research agent — runs multiple tool calls across turns before answering.

---

## Chapter 4: Embeddings, Vector Search & RAG

### 4.1 What Embeddings Represent
- [ ] Theory: text → vectors, semantic meaning as geometry, why "similar meaning" ≈ "close vectors"
- [ ] Practical: embed 5 sentences, print their vectors, manually compare two similar vs two unrelated ones

### 4.2 Similarity Search
- [ ] Theory: cosine similarity, nearest-neighbor search, why it beats keyword search for meaning-based queries
- [ ] Practical: build a tiny in-memory semantic search over 10 sentences, no DB yet

### 4.3 Chunking Strategies
- [ ] Theory: why chunk size matters, overlap, chunking by sentence/paragraph/token count
- [ ] Practical: chunk one document 2 different ways, compare retrieval quality

### 4.4 Vector Databases
- [ ] Theory: what a vector DB adds over manual search (indexing, scale, metadata filtering)
- [ ] Practical: set up Chroma locally, embed and store a folder of documents

### 4.5 Retrieval-Augmented Generation (RAG)
- [ ] Theory: retrieve → stuff into prompt → generate grounded answer, why it reduces (not eliminates) hallucination
- [ ] Practical: build "chat with your PDFs" — ask a question, retrieve relevant chunks, generate an answer citing them

**Chapter 4 Milestone:** Agent can now search your own documents, not just the web.

---

## Chapter 5: Multi-Agent Systems

### 5.1 Agent Roles & Handoffs
- [ ] Theory: why split work across agents (researcher, writer, critic), specialization vs overhead
- [ ] Practical: two agents, one produces a draft, one reviews it — trace the handoff

### 5.2 Orchestration Patterns
- [ ] Theory: sequential vs supervisor vs debate patterns, when each fits
- [ ] Practical: implement a sequential pipeline (research agent → writer agent)

### 5.3 Feedback Loops Between Agents
- [ ] Theory: how a critic agent's feedback gets incorporated, revision cycles, convergence
- [ ] Practical: writer + critic loop, capped at N rounds, log the full negotiation

### 5.4 When Multi-Agent Isn't Worth It
- [ ] Theory: coordination cost, latency, cost multiplication, cases where one strong agent beats many weak ones
- [ ] Practical: compare single-agent vs multi-agent output on the same task — time, cost, quality

**Chapter 5 Milestone:** Writer + critic system that iterates until the critic approves.

---

## Chapter 6: Reliability, Guardrails & Frameworks

### 6.1 Cost & Iteration Limits
- [ ] Theory: why unbounded agents are dangerous in production, budget-based stopping
- [ ] Practical: add a hard cap on tool calls/tokens, test what happens at the limit

### 6.2 Output Validation
- [ ] Theory: schema enforcement, retry-on-failure, why "trust but verify" applies to model output
- [ ] Practical: validate structured output against a schema, auto-retry on failure

### 6.3 Self-Critique / Confidence Checks
- [ ] Theory: having the model assess its own output before finalizing, limits of self-evaluation
- [ ] Practical: add a final confidence-check step before the agent returns its answer

### 6.4 Frameworks (LangGraph / CrewAI / Agents SDK)
- [ ] Theory: what these formalize (state management, loops, handoffs) vs what you built by hand
- [ ] Practical: reimplement your Chapter 3 agent in one framework, compare code and behavior

**Chapter 6 Milestone:** Production-guarded agent + hand-built vs framework comparison.

---

## Capstone
- [ ] Full "Research Assistant" agent: takes a topic → searches web + your documents → plans multi-step research → gets critiqued and revises → produces a sourced report, with guardrails against runaway cost/loops
