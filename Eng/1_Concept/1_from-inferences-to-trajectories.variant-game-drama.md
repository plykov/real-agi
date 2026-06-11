---
title: "1. From Inferences to Trajectories: Memory, the Fan of Scenarios, the Reality Model — a Game-Design and Dramaturgy Variant (working)"
type: article
status: draft
register: private-core
audience: author + aligned (not for open publication)
author: Alex Krol
updated: 2026-05-31
series: "trajectories (1 of 5) — game/drama variant"
---

# 1. From Inferences to Trajectories: Memory, the Fan of Scenarios, the Reality Model

**Private document. Not for open publication.** This is the first of the five essays in the Trajectories series and its foundation. Here I am not building a bridge to someone else's intuition and not persuading from scratch — I am recording, for myself and a narrow circle, my bet on what intelligence is once you stop thinking of it in "query → answer" pairs. Everything that follows in the series stands on this foundation.

**Alex Krol** — strategy, AI, growth infrastructure

[![Version](https://img.shields.io/badge/Version-0.9--draft-orange?style=flat-square)](https://github.com/alexeykrol/real-agi)
[![Website](https://img.shields.io/badge/Website-alexeykrol.com-FF6B35?style=flat-square&logo=safari&logoColor=white)](https://alexeykrol.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Alex%20Krol-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alexkrol/)
[![GitHub](https://img.shields.io/badge/GitHub-alexeykrol-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/alexeykrol)
[![License](https://img.shields.io/badge/©%202026-Alex%20Krol-lightgrey?style=flat-square)](https://alexeykrol.com)

> 🇷🇺 **Russian version:** [Ru/1_Concept/1_from-inferences-to-trajectories.variant-game-drama.md](../../Ru/1_Concept/1_from-inferences-to-trajectories.variant-game-drama.md)

> © 2026 Alex Krol. Private concept document of the Trajectories series. Not for open publication; distribution, quotation, or translation only with the author's explicit written permission.

## Contents

0. [TL;DR — the whole bet on one page](#tldr)
1. [Inference: a single move with no consequences](#1-inference)
2. [The trajectory as the new unit: life is a quest](#2-trajectory)
3. [Not an answer, but a position and a vector in the scenario tree](#3-vector)
4. [The local step versus the productive vector](#4-train)
5. [Scenario space and the reality model](#5-reality)
6. [Finale: navigation is born](#6-navigation)
7. [Glossary](#glossary)

---

## 0. TL;DR — the whole bet on one page <a id="tldr"></a>

My bet fits into a single change of atom. The unit of intelligence is not an answer but a trajectory. Not "give a good answer to a query," but "occupy a productive position in the space of the possible and move in the right direction."

Today nearly the entire stack thinks in inferences — "query → answer" pairs. This is not the nature of intelligence but the form of a memoryless model: a query arrives, a prompt is assembled, an answer is produced, everything is forgotten. A single move with no consequences. Convenient for a business built on API calls, lethal for the idea of a living organism. I change the atom from "model call" to "an episode in the life of an organism" — a trajectory, a quest playthrough in which the agent plans, acts, observes, corrects course, and accumulates experience. The condition that makes such an episode meaningful is long-term, multilayer memory, not a long context.

Then the criterion changes. A linear story, in which the hero meets an obstacle and overcomes it on the spot because otherwise no one would finish reading it, is a poor model of life. In life an obstacle is rarely taken on the first attempt: many attempts, detours, resource gathering, a return to the same wall from another side. Life is not a tale but a quest with a scenario tree. So I optimize not the local accuracy of a move but the vector: where the system is moving within the fan of scenarios, in which direction it is shifting, which branches it opens and closes. This is closer to portfolio management than to finding a felicitous wording. A local error is not frightening if the train is heading in the right direction; a perfect step is useless if the vector is badly chosen. Day trading versus investing.

To generate the fan of scenarios itself, the core needs an explicit reality model — a world with rules in which the quest unfolds at all. I build it from active and reactive elements: active elements generate impact, reactive ones change state in response. A scenario is a chain of such acts, a game loop of "impact → response → signal." The scenario space is the set of typical trajectories on top of this model. On this construction — reality model, scenario space, positioning layer — the entire series stands. In what follows, I unfold each layer.

---

## 1. Inference: a single move with no consequences <a id="1-inference"></a>

Today almost everyone thinks of intelligence in inferences — "query → answer" pairs. The form seems so natural that people have stopped noticing it. Yet it is not the nature of intelligence. It is the imprint of a specific engineering construction — the transformer, with a context window and no state between calls.

The transformer introduced the attention mechanism and a fixed context window: the model looks at the text fed to it and produces a continuation[^1]. This architecture has no recurrent state that would survive a call. Every run starts from a blank slate: everything the model "knows" at the moment of operation is whatever fits into the window right now. Between two calls it remembers nothing. I call this *stateless* — without persisted state. This is neither a defect nor a temporary implementation limitation, but a mode of applying the architecture: the model is a function that takes an input and returns an output, carrying nothing away with it.

In game terms, an inference is a single move with no consequences. Made and forgotten; the next move starts as if the previous one had never happened. In a real game a move changes the state of the world, and you carry that state forward — the entire quest is built on it. With a memoryless call, no state carries over. There is a move, but no playthrough.

Out of this property the entire inference industry grew. Nearly every stack is built as a wrapper around a single call: a query arrives, a prompt is assembled, the model is invoked, an answer comes back, everything is forgotten. Convenient: the call is isolated, easy to meter, to sell by the unit, to scale horizontally. The API business loves memorylessness — it turns intelligence into a token counter. But precisely this memorylessness kills the idea of a living organism before it is even born. An organism that forgets everything after every action is not an organism. It is a calculator with a good vocabulary.

When I look at today's stack, I see not intelligence but a highly capable function without a biography. It can make any individual move brilliantly and can do nothing that requires a playthrough in time: accumulating experience, recognizing a situation the second time around, learning from its own outcomes, holding a course across a series of steps. The layer of "agents" on top of this function most often remains cosmetic. Under the hood is the same memoryless call, wrapped in a loop that imitates continuity by slipping pieces of the past into the window. The imitation works while the quest is short and falls apart as soon as the episode becomes long or important.

I state the diagnosis plainly: thinking in inferences is a legacy of memoryless models, not a form intelligence would have chosen for itself. The "query → answer" pair is convenient as a unit of billing and harmful as a unit of design. If I want to build not a clever API handle but something that lives in time, I need to change the atom itself — to pass from the move to the playthrough. That is what I do next.

---

## 2. The trajectory as the new unit: life is a quest <a id="2-trajectory"></a>

I change the atom. Not a "model call," but an episode in the life of an organism. Not the point "query → answer," but a stretch of time over which something happens: the agent plans, takes several actions, gathers observations, makes mistakes, corrects course, deposits something into memory. I call this stretch a trajectory. In the language of games it is a playthrough — a quest traversed from entry to outcome[^g7].

One distinction is useful here, and it changes everything. A linear story — a tale, a play, a film — is a short product of consumption lasting a couple of hours. In it everything proceeds sequentially: the hero meets an obstacle, then comes the account of how he overcomes it — and he *always* overcomes it, because otherwise no one would finish reading or watching. Life is built differently. An obstacle is often not taken on the first attempt: it requires repeated approaches, detours, resource gathering, retreating and returning to the same wall from another side. So life is modeled more accurately not by a linear story but by a quest — with a scenario tree, retries, and a game loop in which every move changes something in the state of the world[^g3]. The story lies about how obstacles are taken; the quest tells the truth. This transition from the linear story to the nonlinear quest is the transition from inference to trajectory.

The shift seems small, but it rebuilds everything. As soon as the basic entity is not the inference but the playthrough, an axis of time appears — something a memoryless model lacks in principle. Along this axis one can compare: one playthrough led to a result, another ran into a wall — a failure state from which there is no further move[^g6]. One can select successful moves and cull dead-end branches. One can teach the system not to "give the best answer to this input" but to "run the scenario better than last time." What matters becomes not only the finale but the path: which decisions were made, what the agent saw, where it took a wrong turn, which resources it gathered, what it added to memory. The final answer is merely the last point of the stretch, and far from always the most important one.

The formulation of the task changes along with the atom. Instead of "produce an answer for me" — "run a scenario of interaction with a system, a user, or a market, and update your internal state." This is already the language of an organism running a quest, not of a function answering a stimulus. An organism does not react and forget; it acts drawing on its entire history and exits the episode different from how it entered.

Here lies the boundary that is easy to miss. The condition that makes a trajectory meaningful is not a long context but long-term, multilayer memory. These are different things. A long context is simply a large window into which more text can be stuffed in a single call; it still resets to zero at the end. Memory is a structure that survives calls and accumulates between episodes. Without it the playthrough is illusory: outwardly the agent travels a long path, while inside it still starts from a blank slate at every move. In a game this is a save that failed to write: after every move you are rolled back to the start of the level, and the resources you gathered disappear.

The memory that makes a trajectory real I think of as several layers with different lifetimes. Session memory, short-term — everything within a single run or dialogue, what is needed right now and goes away on completion. Episodic — the histories of specific playthroughs: cases, projects, deals lived from start to finish, with their outcomes. Semantic — a distillate of facts, patterns, and preferences detached from any specific episode: what is true in general about this world, this user, this type of situation. And the top layer — insights: aggregated lessons derived from many episodes and read on every new launch. Not "what happened in case number 47," but "with this type of situation, don't do that." The division into these four layers is mine, made for my task; the academic landscape describes agent memory differently and more broadly[^8], but the logic is the same everywhere: an external long-term store plus a mechanism for retrieving relevant pieces into the window before each move.

Modern agents with memory are built roughly this way and already resemble an organism running a quest noticeably more than a bare call does. Hierarchical memory, where a fast layer works with a slow one by analogy with an operating system's memory, is a working engineering scheme[^2]. A stream of observations that is periodically condensed into reflection and feeds planning is a working way to obtain that very top layer of distilled lessons[^3]. I do not pass these works off as confirmation of my four-layer scheme specifically — I slice the layers for my own purposes. I rely on what is established: memory that survives calls turns a reacting function into an acting organism. And what an organism needs is no longer the best reply. It needs to understand where it is moving along the scenario tree.

---

## 3. Not an answer, but a position and a vector in the scenario tree <a id="3-vector"></a>

As soon as the trajectory becomes the unit, the main question shifts. It stops being the question "what answer to give" and becomes the question "what position to occupy." I stop asking the system about the relevance of an individual reply and start asking about its position and vector relative to the entire fan of possible scenarios.

The fan of scenarios is the set of trajectories that are in principle reachable from the current point; in game terms it is a scenario tree with branching, the possibility space through which the agent moves[^g3]. Around a user, a product, a market, a channel, different possible playthroughs unfold, and every move opens some branches and closes others. At each moment the system faces not the choice "what to write" but the choice of a position within this tree. Which scenario to unfold now. In which direction to shift the trajectory — riskier or more conservative, deeper into the known or wider into the unexplored. Which future branches to open and which to close, sometimes irreversibly. An individual answer, against this background, is merely a small move along an already chosen vector. The object of control is the vector itself — the choice of a branch in the tree.

A branch here is not just a synonym for a scenario. It is the game mechanic of choice: a move opens some passages and closes others, sometimes irreversibly, like a door that latches behind your back. Every playthrough leaves a trace — what outcome the branch produced, what resource was gathered on it — and this trace is not discarded but is deposited into memory as experience points: the signal by which the tree is marked up for the next run. A player going through a level not for the first time moves across a map already marked up; a memoryless function enters the tree blind every time.

One of the pivotal choices of this layer has a canonical name in the theory of reinforcement learning: *exploration/exploitation* — the balance between exploring new branches and exploiting a known good one[^4]. To exploit is to press where the system already knows what works and collect a predictable return, a proven reward. To explore is to spend a move on a branch with an unclear outcome, for the sake of information that may overturn the strategy. A memoryless function does not even see this choice: it has no past from which to know "what works" and no future for whose sake to explore. For an organism running a quest with memory, this balance is an everyday decision, and holding it is the job of the layer that thinks about the position in the tree, not about an individual move.

This shift takes me far from classical language processing and brings me to control theory and portfolio thinking. Control theory has a precise construction describing exactly this logic: planning-horizon control, *receding horizon* — at every step a trajectory is optimized over a horizon ahead, only the first step is executed, the window slides, and everything repeats[^6]. The local action is subordinated to the plan over the horizon, not the other way around. This is exactly my stance: the move serves the vector; the vector is not assembled from moves. The value of a move is measured not by its own quality but by how it shifted the system's strategic position in the tree — in business metrics, in information gained, in risk, in accumulated experience.

From this, what the core must be also changes. If it thinks in inferences, it remains a query router — accepts an input, picks a tool, returns an output. If it thinks in position and vector, it becomes a strategic planning layer that holds the map of scenarios and the current point on it. This layer draws on long-term memory directly: episodic memory stores traversed trajectories and their outcomes, so that it is clear how different vectors behaved over time; semantic memory stores models of the scenarios themselves — which types of branches exist and in which contexts they have worked; the insight layer stores derived positioning rules of the kind "in this market phase, strategy X dominates Y." The organism's self-development at this level is not "we answer the same questions better" but "we weight the scenario tree differently and occupy different positions relative to the future." This is no longer about the move. It is about which direction the entire playthrough is going.

---

## 4. The local step versus the productive vector <a id="4-train"></a>

Here is the heart of my bet. A local deviation over a short stretch matters less than the productive vector. What to do is less important than where to go and which trajectory you are on. This distinction has long been formalized in the very mechanics of games: a single move within the rules is one thing, strategy as a plan for distributing moves toward the win condition is another, and it is the strategy that wins, not an individual lucky move[^g3]. What matters is always to end up on the train that is heading in the right direction.

I choose the train image not for ornament but because it precisely separates two levels that are constantly confused. A local deviation is an individual inference, a single move along the rails. The agent phrased something imperfectly, picked the wrong tool, slightly missed the tone, gave a seven-out-of-ten answer instead of a nine. That is noise along the line. The productive vector is the chosen trajectory and the train: what strategy the system is playing at all right now, which funnel, campaign, or process it is in, and whether that process leads, in principle, where it needs to go. You can make a flawless move on a train going the wrong way, and every perfect move will carry you farther from the goal. And you can stumble at every step on the right train and still draw closer. The geometry of the movement matters more than the quality of an individual move.

And exactly here one can see why the quest is more accurate than the story. In a linear story a flawless move always leads to victory — otherwise the author rewrites the scene. In a quest you can play a fight perfectly and discover that you are on the wrong branch of the tree altogether: the wrong resource was gathered, the door to the finale was left behind your back, and the more cleanly you play this dead end, the deeper into it you go. The cost of error here lies not in the quality of the move but in which scenario you are on and where it leads — these are the stakes of the playthrough, not the neatness of an individual action[^d1].

The best analogy for this difference is day trading versus investing. Answers and inferences are day trading. The accuracy of a specific reply, the felicity of a wording, the choice of one tool call over another, the fine-tuning of prompts, of schemes for mixing in knowledge from external memory — I call this *RAG*, retrieval of the relevant before answering — endless retries. One can do all of this to the point of exhaustion, the way a trader churns intraday deals chasing tick-level movements. And exactly as with a day trader, the main risk here is burning out in the micro-optimization of a single move and failing to notice that the global vector is badly chosen: wrong niche, wrong audience, wrong model. A move polished to a shine inside a losing strategy is a perfectly executed trade against the trend.

The choice of vector and trajectory is investing. The question is not "how to play this move best" but "which asset and which strategy you are in": which vertical, which funnel, which class of scenarios is scaling. What works here is not the quality of an individual trade but the distribution across trains, the planning horizon, and the cumulative effect of decisions. A local minus — an imperfect post, a less-than-best answer — is not frightening if the portfolio as a whole is moving in the right direction. This is the direct logic of portfolio theory: value is determined not by an individual position but by the configuration of the portfolio in the coordinates of risk and return, and a single drawdown decides nothing if the composition is right[^5]. I transfer this logic from assets to scenarios: the investor-intelligence manages a portfolio of trajectories rather than polishing every move.

From this follows what the core must be. Not a day trader churning individual inferences, but an investor managing a portfolio of scenarios. The principal intelligence lies in choosing which scenarios to launch, which to scale, which to wind down, and how to redistribute the capital of attention and compute among them. Not in bringing every move to perfection. And then the local flaws of the action layer cease to be a threat: the organism has time to compensate for them, because globally it is moving along the right trajectories, like a player who clears the level not cleanly but through the right door. The phrase "always end up on the train heading in the right direction" is an invariant I build into the system as a primary requirement. At every moment it must be able to answer: which scenario are we in now, where is it leading by the key metrics, and is it time to change trains because the current one has stopped going where it should. The scenario and its vector become what is optimized. Individual answers are micro-noise along the line.

---

## 5. Scenario space and the reality model <a id="5-reality"></a>

To recommend where to move rather than what to answer, the core needs an explicit model of the scenario space. Not a base of facts, but a map of trains and routes — a tree of possible playthroughs. And immediately a question one level deeper arises: where does this map come from. The scenario space is not given in advance — something has to generate it. For me, that something is the reality model: a world with rules, in which the quest unfolds at all[^g1].

First, about the space itself. What lives in the core is not only documents and knowledge but scenarios as first-class entities: chains of steps with goals, entry and exit conditions, success metrics. Mechanically, each scenario is a game loop, a core loop: an impact produces the world's response, the response yields a signal, the signal determines the next impact, and so on around the circle[^g8]. Each scenario is a train with its own direction: interaction format, user type, horizon, risk regime. The scenario space is the set of such trains plus the links between them: which branches one can transfer to, which scenarios are incompatible, which reinforce one another. A recommendation in such a system is not "pick the best answer" but "pick a scenario and a position in this space": which train to put the process on, along which trajectory to lead it, when to propose a transfer to another branch. The positioning layer looks at the organism's state — history, context, current metrics — projects it into the scenario space, finds candidates by goals and constraints, picks the train and the vector within it, and only then hands this down to the action layer, which fills the route with concrete inferences and tool calls.

But the map of trains does not hang in a void. To generate it, a reality model is needed — the game world with its rules — and I build it from active and reactive elements. Active elements generate impact: they initiate actions, change conditions, launch scenarios. The method by which an active element acts on the world is its mechanic[^g2]. These are the agents themselves, users, external actors such as the market and competitors, my automated processes. They choose which train to launch and where to apply effort. They also include forces the agent does not control — the market, trends, audience behavior, competitors: the probabilistic active forces of the world, which cannot be predicted exactly but can be caught with statistics. Reactive elements respond to impact by changing their state: they update data, metrics, context, statuses. These are databases, logs, business indicators, funnel states, infrastructure, the audience as an aggregate of views, clicks, retention. They record how the world actually changed in response to activity. Reality in this model is a field where active elements continuously fire off impacts and reactive ones update the map by which I build the next scenarios. Thus the feedback loop of the game loop unfolds to the scale of the entire world.

From this division the scenario space is derived directly. A scenario is a sequence of acts: an active impact produces a reactive change, that yields a new state, from which a new impact follows, and so on. That very core loop. And this loop is almost never completed on the first run: the impact runs into a reactive wall that did not yield, the state changes the wrong way, and the active element goes in for a retry — with a different strike, by a detour, after first gathering the missing resource on a neighboring branch. A scenario in the core is therefore not a straight line but a loop with retries: a typical trajectory is not a single pass but a schema of how an active element takes an obstacle over several attempts. Each scenario is marked up by which active element presses on which reactive parts of the system, with what goal, and in what sequence — and how many runs it takes on average for the reactive part to budge. The scenario space is the set of such trajectories, marked up by who acts, on what, over which horizons, and by which metrics. And then the recommendation takes its final form: which active element to be right now, which reactive parts of the world to strike, which typical trajectory to follow. The positioning layer works not in a vacuum but on an explicitly specified model of the world — who is active, what is reactive, how they are connected.

I lean here on a general thesis with an academic pedigree: to generate scenarios, an agent needs an internal model of its environment, on which it plans and plays variants forward[^7]. The division into active and reactive elements is mine; I do not attribute it to that line of work — I take from it only the right to say that without a reality model, scenario planning is impossible in principle. And I need that right because the cost of lacking such a model is concrete. Without it, an agentic system degenerates into an advanced chatbot: there is no clear division of who acts and what exactly changes as a result of actions; the scenario space blurs into a set of prompt chains instead of a structure of influence on the world; there is nothing to optimize over the long run, because it is unclear which strikes on the system produce the needed restructuring of state. But if active and reactive elements are specified as first-class entities of the core, everything becomes measurable: scenarios are described as combinations of strikes by the active on the reactive, one can measure how different trajectories actually restructure the system, and one can construct that very productive vector — the sequence of impacts that brings the organism into the desired configuration. The reality model — active and reactive elements; the scenario space — typical trajectories of acts on top of it; the positioning layer — the choice of which active element to be and which reactive ones to work through. This order is not accidental, and the layers cannot be rearranged.

---

## 6. Finale: navigation is born <a id="6-navigation"></a>

The three layers assemble into a single vertical, and in it emerges what all of this was from the very beginning. At the bottom — the reality model built from active and reactive elements, the game world with its rules. On top of it — the scenario space as a tree of typical trajectories. Above that — the positioning layer, which chooses which active element to be and which reactive ones to strike, which branch to hold. From the bottom up, this ceases to be an answering machine and becomes navigation. The system does not answer queries. It plots a course through a world with rules, stakes, and outcomes[^d2].

And here one can see why I have been speaking in the language of the quest all along, not of the story. A story is linear: a single pass, the hero always wins, the obstacle always falls on the first attempt. Life and intelligence are not built that way. They are nonlinear: a scenario tree, retries, detours, resource gathering, branches that moves open and close, trains between which one can and must transfer. That is exactly why the atom is the trajectory, not the inference; that is exactly why what matters is the vector and the drift, not the quality of an individual move. A single flawless move is, at best, a beautiful scene in a lost playthrough. What is valuable is not the move but how the accumulated moves and the chosen vector shift the organism along the tree toward the needed outcome.

The captain of this system needs exactly one thing — where to lead. Not a perfect individual move at minute fifteen, but the productive vector given the current configuration of the world's rules and the observed statistics of its forces. The same train invariant: what matters is not the accuracy of the move but the direction of the playthrough. The system is not a clever executor of a single move but a navigator across the scenario tree of an entire life; from this vantage it is natural to think not in inferences but in courses, branches, stakes, and a portfolio of routes. But what, in the concrete verticals of life, turns out to be the rules of the world, what — probabilistic forces, which agents move there, and how the navigator decides which branch to take in the next sprint — that is another map. I unfold it in the next text.

---

## Sources

[^1]: Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention Is All You Need. *Advances in Neural Information Processing Systems 30* (NeurIPS 2017). https://arxiv.org/abs/1706.03762

[^2]: Packer, C., Wooders, S., Lin, K., Fang, V., Patil, S. G., Stoica, I., & Gonzalez, J. E. (2023). MemGPT: Towards LLMs as Operating Systems. *arXiv preprint* arXiv:2310.08560. https://arxiv.org/abs/2310.08560

[^3]: Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative Agents: Interactive Simulacra of Human Behavior. *Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology* (UIST '23). https://arxiv.org/abs/2304.03442

[^4]: Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press. http://incompleteideas.net/book/the-book-2nd.html

[^5]: Markowitz, H. (1952). Portfolio Selection. *The Journal of Finance*, 7(1), 77–91. https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1952.tb01525.x

[^6]: Rawlings, J. B., Mayne, D. Q., & Diehl, M. M. (2017). *Model Predictive Control: Theory, Computation, and Design* (2nd ed.). Nob Hill Publishing. https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf

[^7]: Ha, D., & Schmidhuber, J. (2018). World Models. *arXiv preprint* arXiv:1803.10122. https://arxiv.org/abs/1803.10122

[^8]: Zhang, Z., Bo, X., Ma, C., Li, R., Chen, X., Dai, Q., Zhu, J., Dong, Z., & Wen, J.-R. (2024). A Survey on the Memory Mechanism of Large Language Model based Agents. *arXiv preprint* arXiv:2404.13501. https://arxiv.org/abs/2404.13501

[^g1]: Schell, J. (2008/2019). *The Art of Game Design: A Book of Lenses* (3rd ed.). Boca Raton, FL: A K Peters/CRC Press (Routledge). https://www.routledge.com/The-Art-of-Game-Design-A-Book-of-Lenses-Third-Edition/Schell/p/book/9781138632059

[^g2]: Sicart, M. (2008). Defining Game Mechanics. *Game Studies*, 8(1). https://gamestudies.org/0801/articles/sicart

[^g3]: Salen, K., & Zimmerman, E. (2004). *Rules of Play: Game Design Fundamentals*. Cambridge, MA: MIT Press. https://mitpress.mit.edu/9780262240451/rules-of-play/

[^g6]: Juul, J. (2013). *The Art of Failure: An Essay on the Pain of Playing Video Games*. Cambridge, MA: MIT Press. https://mitpress.mit.edu/9780262019057/the-art-of-failure/

[^g7]: Juul, J. (2005). *Half-Real: Video Games between Real Rules and Fictional Worlds*. Cambridge, MA: MIT Press. https://mitpress.mit.edu/9780262516518/half-real/

[^g8]: Core loop / game loop — an established term of game-design practice with no single monograph as its primary source; the repeatable basic sequence "action → response/signal → progression → action again." https://www.gamedeveloper.com/business/why-the-core-gameplay-loop-is-critical-for-game-design

[^d1]: McKee, R. (1997). *Story: Substance, Structure, Style, and the Principles of Screenwriting*. New York: ReganBooks/HarperCollins. https://mckeestory.com/do-your-scenes-turn/

[^d2]: Aristotle. *Poetics* (Περὶ ποιητικῆς), ca. 335 BC. https://en.wikipedia.org/wiki/Poetics_(Aristotle)

---

## Glossary <a id="glossary"></a>

**Inference** — a "query → answer" pair: an isolated model call in which a query arrives, a prompt is assembled, an answer is produced, and everything is forgotten. In this essay — the unit I reject as the atom of intelligence; in game terms it is a single move with no consequences: there is a move, but no playthrough.

**Stateless model** — a model without persisted state between calls: a function that takes an input and returns an output, carrying nothing away with it. Every run starts from a blank slate; this is a mode of applying the transformer architecture, not an implementation defect.

**Context window** — the fixed volume of text the model sees in a single call. It resets to zero at the end of the call; everything the model "knows" at the moment of operation is only what fits into the window right now.

**Long context** — a large context window into which more text can be stuffed in a single call. In the essay it is contrasted with memory: the window still resets at the end and does not make the trajectory real. In the game picture — a save that failed to write: after every move, a rollback to the start of the level.

**Trajectory** — a stretch of time over which the agent plans, acts, observes, makes mistakes, corrects course, and accumulates experience. The new atom of intelligence in place of the inference; in the language of games — a playthrough, a quest from entry to outcome.

**Quest** — *(a borrowed game-design concept)* a playthrough of a world with rules, from entry to outcome, through obstacles, attempts, and resource gathering. In the essay — an accurate model of life in place of the linear story: an obstacle is rarely taken on the first attempt, which is why life is nonlinear.

**Scenario tree (branching)** — *(a borrowed game-design concept, branching)* the structure of choice in the possibility space: a move opens some branches and closes others, sometimes irreversibly. In the essay — the game form of the fan of scenarios: the object of control is not an individual move but the choice of branch.

**Failure state** — *(a borrowed game-design concept, failure state)* a dead end from which there is no further move; a branch that has run into a wall. In the essay — what a failed playthrough runs into, as opposed to a branch leading to an outcome.

**Episode in the life of an organism** — the same as a trajectory, phrased as the change of atom: "model call" is replaced by "episode," from which the organism exits different from how it entered. It draws on its entire history rather than reacting to a stimulus.

**Memory (long-term, multilayer)** — a structure that survives calls and accumulates between episodes; the condition that makes a trajectory meaningful, as opposed to a long context. Without it the playthrough is illusory: outwardly the path is long, inside the agent starts from a blank slate at every move.

**Session memory** — the short-term layer: everything within a single run or dialogue, needed right now and gone on completion.

**Episodic memory** — the histories of specific playthroughs: cases, projects, deals lived from start to finish with their outcomes. It stores traversed trajectories and their outcomes, so that it is clear how different vectors behaved over time.

**Semantic memory** — a distillate of facts, patterns, and preferences detached from any specific episode: what is true in general about this world, a user, a type of situation. It also stores models of the scenarios themselves — which types of branches exist and where they have worked.

**Insight layer** — the top layer of memory: aggregated lessons derived from many episodes and read on every new launch. Not "what happened in case number 47," but "with this type of situation, don't do that"; it stores positioning rules.

**Fan of scenarios** — the set of trajectories in principle reachable from the current point; in game terms — a scenario tree with branching, a possibility space. At each moment the system chooses not "what to write" but a position within this set.

**Experience points (the signal that feeds memory)** — *(a borrowed game-design concept, reward/score)* the trace every playthrough leaves: what outcome the branch produced, what resource was gathered. In the essay — the markup of the scenario tree, deposited into memory so that the next run proceeds across a map already marked up.

**Position** — the system's location within the fan of scenarios: which scenario is unfolding now and what the risk regime is. The main question shifts from "what answer to give" to "what position to occupy."

**Productive vector** — the direction of the system's movement in the fan of scenarios: where the trajectory is shifting, which branches it opens and closes. The object of control in place of an individual answer; the move serves the vector, the vector is not assembled from moves.

**Move versus strategy** — *(a borrowed game-design concept, move vs strategy)* a single move within the rules versus a plan for distributing moves toward the win condition; it is the strategy that wins, not an individual lucky move. In the essay — the canonical support for the distinction "local step vs productive vector."

**Positioning layer** — the strategic planning layer that holds the map of scenarios and the current point on it, chooses the train and the vector, and only then hands this down to the action layer. It projects the organism's state into the scenario space and draws on long-term memory directly.

**Action layer** — the lower layer that fills the chosen route with concrete inferences and tool calls. Its local flaws are not a threat if globally the system is moving along the right trajectories.

**Local step (local deviation)** — an individual inference, a single move along the rails: an imperfect wording, the wrong tool, a missed tone. Noise along the line, less important than the choice of vector.

**Drift** — the displacement of a trajectory under the effect of accumulated moves and the vector; in the essay it is expressed through the image of a train that either heads in the right direction or carries you ever farther from the goal with every perfect move. The geometry of movement matters more than the quality of an individual move.

**Stakes of the playthrough** — *(a borrowed dramaturgy concept, stakes)* the cost of which scenario you are on and where it leads, as opposed to the neatness of an individual action. In the essay — a layer shared with the game: the risk regime of a position, not a linear narrative structure.

**Exploration / exploitation** — *(a borrowed concept from reinforcement learning)* the balance between exploring new branches and exploiting a known good one. In the essay — the pivotal choice of the positioning layer, one that a memoryless function does not even see.

**RAG** — retrieval of relevant pieces from external memory and mixing them into the window before answering. In the essay it is assigned to "day trading": fine-tuning the delivery of knowledge at the level of an individual move, not the choice of vector.

**Day trading versus investing** — the author's metaphor for the two levels. Day trading — the accuracy of an individual reply, the choice of a call, prompt tuning, endless retries; the main risk is burning out in micro-optimization while the global vector is badly chosen. Investing — the choice of vector and trajectory: which asset, niche, funnel, and class of scenarios you are in.

**Portfolio of scenarios** — the author's metaphor: the core as an investor managing the distribution of the capital of attention and compute among scenarios, not a day trader churning individual inferences. Which scenarios to launch, scale, wind down, and how to redistribute among them.

**Portfolio theory** — *(a borrowed concept, Markowitz)* value is determined not by an individual position but by the configuration of the portfolio in the coordinates of risk and return, and a single drawdown decides nothing if the composition is right. In the essay it is transferred from assets to scenarios — the justification for why a local minus is not frightening if the portfolio of trajectories is right.

**Receding horizon / MPC** — *(a borrowed concept from control theory)* at every step a trajectory is optimized over a horizon ahead, only the first step is executed, the window slides, everything repeats. In the essay — the precise construction behind the stance "the local action is subordinated to the plan over the horizon, not the other way around."

**"Which train you are on"** — the author's metaphor for the productive vector: the type of strategy, funnel, campaign, or process the system is in, and whether it leads where it needs to go. A flawless move on a train going the wrong way carries you away from the goal; the invariant is "always end up on the train heading in the right direction."

**Scenario space** — the explicit map of trains and routes in the core: the set of scenarios plus the links between them (which one can transfer to, which are incompatible, which reinforce one another). Not a base of facts but a structure by which position and vector are chosen; it is derived from the reality model.

**Scenario** — a first-class entity of the core: a chain of steps with goals, entry and exit conditions, success metrics; a typical trajectory of acts "active impact → reactive change." Mechanically — a game loop, a core loop, and not a straight line but a loop with retries: a schema of how an active element takes an obstacle over several attempts.

**Game loop (core loop)** — *(a borrowed game-design concept, core loop)* the repeatable basic sequence "impact → response → signal → next impact." In the essay it is mechanically identified with the scenario as a chain of acts; it unfolds to the scale of the entire world as a feedback loop.

**Mechanic** — *(a borrowed game-design concept, game mechanic)* the method by which an active element acts on the world. In the essay — the way an active element initiates an action and changes the state of reactive parts.

**Reality model** — the bottom layer of the vertical, the one that generates the scenario space; it is built from active and reactive elements. It is the game world with its rules, in which the quest unfolds at all; without it, scenario planning is impossible in principle, and an agentic system degenerates into an advanced chatbot.

**Active elements** — that which generates impact: initiates actions, changes conditions, launches scenarios. Agents, users, external actors such as the market and competitors, automated processes; they also include the probabilistic forces of the world (the market, trends, audience behavior), which cannot be predicted exactly but can be caught with statistics.

**Reactive elements** — that which responds to impact by changing its state: data, metrics, context, statuses. Databases, logs, business indicators, funnel states, infrastructure, the audience as an aggregate of views and clicks — they record how the world actually changed.

**Game world (environment model)** — *(a borrowed concept: game design, game world; agent theory, World Models)* the world as a constructed space, defined by rules and setting, on which the agent plans and plays variants forward. In the essay — the right to claim that without a reality model, scenario planning is impossible; the division into active and reactive elements I do not attribute to that line of work.

**Navigation** — what the entire vertical, from the bottom up, turns out to be: the system does not answer queries but plots a course through a world with rules, stakes, and outcomes. The reality layer, the scenario space, and the positioning layer together cease to be an answering machine.
