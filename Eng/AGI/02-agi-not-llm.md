### Chapter 2. Not LLM, but AGI


**Alex Krol** — strategy, AI, growth infrastructure

[![Version](https://img.shields.io/badge/Version-0.9--draft-orange?style=flat-square)](https://github.com/alexeykrol/real-agi)
[![Website](https://img.shields.io/badge/Website-alexeykrol.com-FF6B35?style=flat-square&logo=safari&logoColor=white)](https://alexeykrol.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Alex%20Krol-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alexkrol/)
[![GitHub](https://img.shields.io/badge/GitHub-alexeykrol-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/alexeykrol)
[![License](https://img.shields.io/badge/©%202026-Alex%20Krol-lightgrey?style=flat-square)](https://alexeykrol.com)

> © 2026 Alex Krol. All rights reserved. Republication, redistribution, or commercial use only with the author's explicit written permission.

Over the past two years, the word "AGI" has entered the mass vocabulary and instantly worn itself smooth. People slap it on everything: the next generation of GPT, a new model from a startup that needs your investment, any system slightly better than the last one. At conferences they swear by it. In headlines they scare you with it. In ads they sell with it.

And almost no one who says "AGI" distinguishes it from what we already have.

This distinction is not academic nitpicking. The entire conversation that follows rests on it. If in chapter one I reframed the question from "where will demand for humans survive" to "what advantage does a human have over AGI," now I need to say what exactly stands on the other side of the comparison. Because if the reader plugs in GPT-4 in a browser tab, they will easily calm down and close the book. Compared with GPT-4, we come out ahead almost everywhere. Compared with AGI — almost nowhere.

Today's language models are very large next-token predictors, trained on enormous corpora of text and polished to the point where their output is coherent, grammatical, and in a large share of cases meaningful. They can hold a conversation, write code, explain concepts, translate, summarize, crack jokes. They are a powerful tool. But they have hard limits: they operate inside the statistics of what has already been said. They do not step outside those statistics. Their "reasoning" is pulling longer and more structured chunks out of a learned probability distribution than before. Nothing more.

That's why, talking to GPT-5, any competent user sooner or later catches the moment: here it starts to flounder. Here it didn't understand the task. Here it delivered a mealy-mouthed answer with a confident face. These moments give a pleasant feeling of intellectual superiority. "Sure, it's a smart machine, but not a real interlocutor." And nearly all the consolation literature about the future of human work is built on that feeling.

The trouble is, that feeling is temporary by its very nature.

Because AGI is not "a smarter GPT." AGI is a different category of system. A system that has not one narrow function honed to high quality, but **general cognitive breadth**: comparable to a human in general cognitive breadth and consistently superior to 90% of people in the quality of decisions — in any subject area whatsoever. Not "it writes better texts." It diagnoses better. Designs better. Manages better. Investigates better. Teaches better. Makes better decisions in a new situation no one has ever described before. And all of it in one head, with no switching between experts.

The distinction can be shown through a familiar piece of tech history. In 1997, the chess engine Deep Blue beat Kasparov. It was a narrow system built for a single game: position evaluation, search through a tree of variations, a huge database of games. You couldn't transfer Deep Blue to another task — it could do nothing but chess. Twenty years later, AlphaZero was learning chess, Go, and shogi "from scratch," from the rules alone, without human games. That was a more general architecture — but still limited to games with clear rules and a clear success function. AGI is the next and fundamentally different step. A system that, besides chess, also understands law, and cardiology, and bridge design, and raising a child, and crisis management — at a level comparable to the best specialists in each of those fields. And it has no field "of its own"; its field is any task that can be posed at all.

When, in the original dialogue, I tried to pin this framing down hard — not "where is a human stronger than GPT," but "where will a human still be needed once AGI arrives" — my interlocutor pushed the formulation to its most uncomfortable form. Here it is as it happened.

> **[from the dialogue]**
>
> **ChatGPT:** *The real question is different: not where AI will replace humans, but where a human will still be needed even with AGI in the picture. In other words, not where a human is stronger than today's language models, but where the world will still need humans even when an AGI appears that is comparable to a human in general cognitive breadth and consistently superior to 90% of people in the quality of decisions.*

This formula — AGI as a system comparable to a human in general cognitive breadth and consistently superior to 90% of people in the quality of decisions — will be the anchor of this book. If at some point further on you lose the thread of what we're comparing with what — come back to it. Any attempt to shift the conversation back to "but GPT-5 still makes mistakes" is an attempt not to enter the uncomfortable conversation at all.

No such system exists today. And that needs to be said honestly, right away. No current product — not ChatGPT, not Claude, not Gemini, not the Chinese models — is AGI. All of them have failure modes easily exposed under minimal load. They hallucinate. They get lost in long chains of reasoning. They can't set a task for themselves. They don't work long and autonomously on a complex project without a human operator. None of that is AGI; it's transitional technology.

But transitional is the key word. Between what exists and what I described above as AGI, there is no ontological gap that would guarantee one never turns into the other. There are engineering problems. Very big ones. Very expensive ones. Very unsolved ones. But not forbidden ones.

Before going further, I need to say one thing about timelines — and close the subject immediately, because it steals attention.

When you ask different people who work on AI professionally when AGI will arrive, the answers diverge wildly. Some say five years. Some say twenty. Some say half a century. Some say the current transformer architecture will never lead to AGI and fundamentally different approaches are needed. All of these positions have their grounds. I'm not going to dissect them, and I'm not going to bet on a specific number. This is not a book about forecasting timelines. This is a book about a question that matters under any timeline.

The logic here is simple. Every horizon is a concrete life situation, not an abstraction.

Ten years means we ourselves will have to live in that world — at a mature age, with settled habits and settled competencies. Twenty means it's the careers of our children, whom we are right now sending into schools and universities that prepare them for a labor market that will change beyond recognition by the time they graduate. Fifty means it's the culture we are shaping now, and the educational systems graduating people into professions that forty years from now won't exist in their current form. And if AGI never arrives — which I consider unlikely but possible — the question of the boundary of human advantage over powerful machine intelligence still stands, because even without AGI, systems are already appearing that outperform most people on certain broad classes of tasks. Knowing the limits of your own advantage is intellectual hygiene at its most basic. Not knowing them is the ostrich position, and it protects nothing.

So whichever way you approach it, the question stands. Arguing about timelines is a way to postpone the conversation about substance, smothering it under a cotton-wool blanket of "let's wait until the picture clears up." The picture won't clear up. Decisions get made before forecasts converge.

When I reframed the question in the original dialogue as a comparison with AGI, my interlocutor first reacted in the standard way: it tried to separate "demand for humans" and "advantage over AGI" as different things. The idea being that demand can persist where a human no longer has any real advantage — through habit, trust, regulation, cultural inertia. That's a correct observation, but it steered the conversation away from where I wanted it. I didn't want to separate the rational from the irrational; I wanted to show that the irrational advantage is temporary too. That the market gradually learns to measure outcomes, and the cultural head start given to the "human touch" melts away over the long run.

I'm quoting the exchange as it went, because you can clearly see the formulation ripening in it.

> **[from the dialogue]**
>
> **Me:** *Here you're wrong, because you've restricted everything to rational choice, but demand is almost always irrational, which is why choosing a human — because they're human — is precisely an example of an advantage. But my thesis is that, gradually, irrational choice gives way to rational choice.*
>
> **ChatGPT:** *Yes, that's an important correction. I really did draw too hard a line between "rational" and "irrational," as if demand were determined by efficiency alone. Your thesis is subtler: irrational demand for a human is, in itself, also a real market advantage for the human. You simply hold that this advantage is unstable and erodes over time as the market learns to compare by outcome.*

This correction matters specifically for the chapter on AGI, not just the one on the market. Because the entire consolation genre of "where humans will remain" is built on conflating two time horizons. On the short one — yes, there will be room for humans in plenty of places, for reasons that have nothing to do with any real superiority. Habit, regulation, fear of the new, sentiment, the aesthetics of authenticity, the symbolic value of "made by a human." All of this gives people jobs. All of this gives people a place in the world. And none of it survives the encounter with mature AGI, because these reasons are transitional. They hold a person in places where they have no advantage exactly until the alternative becomes cheap enough, convenient enough, and good enough. Then the culture relearns. Not in five years. But over twenty or thirty it relearns every time, in every historical era, whenever the alternative turns out to be consistently better.

So when people say "AGI is nothing to fear, because people will always need living people" — that's a statement about today and the next ten years or so, not about the steady state. And the book you are reading now is about the steady state, not the transition period.

Here I need to introduce an important restriction that will save us from pointless arguments more than once down the road.

In this book, AGI is defined **functionally**, not metaphysically. It is a system comparable to a human in general cognitive breadth and consistently superior to 90% of people in the quality of decisions. Period. AGI under this definition is not required to be "conscious." Not required to have self-awareness. Not required to feel. Not required to want. Not required to ask "who am I." Not required to be what a philosopher would call a person.

This is deliberate. Because the question of AI consciousness is a separate one — very deep, deserving its own conversation, which we will get to later. Mixing it with the question of cognitive power means zeroing out the entire conversation from the start. If you demand "real consciousness" from AGI, you can postpone its arrival indefinitely: until it's proven that the machine "truly feels," it's "not real AGI" — and the human, supposedly, is safe. It's a convenient rhetorical trap, and it means nothing, because **functionally** a machine can push a human out of any cognitive task without "feeling" anything in the process. A crane doesn't feel — and it lifts loads better than a human. A calculator doesn't feel — and it computes faster. If AGI doesn't feel but treats patients better than a doctor, designs better than an engineer, and investigates better than a detective — then for the labor market, for the professions, for the social order, the difference between a "feeling AGI" and a "non-feeling AGI" is almost nil. The social and economic effect is one and the same.

Why is the functional definition here not a philosophical concession but exactly what's needed? Because our conversation is not about the nature of mind. It's about advantage. And advantage, unlike mind, is tested from the outside, by results. The market doesn't ask a doctor whether he feels. The market asks whether the patient survives. The employer doesn't ask an engineer whether the design moves them. The employer asks whether the bridge holds. Careers aren't built on the ontology of your own consciousness; careers are built on the fact that after your intervention in reality, reality is better off than after your neighbor's. If the neighbor is a human, you're competing with a human. If the neighbor is a machine, you're competing with a machine. In both cases, the criterion is the same.

The metaphysical definition of AGI — "real mind," "true consciousness," "genuine understanding" — is a definition under which it's convenient to do nothing. Nothing will ever qualify, because no one knows how to test such a definition. The functional definition is inconvenient precisely because it is testable. If not today, then tomorrow. If not this version, then the next. And that's exactly why it works. So, to avoid sliding into a long philosophical discussion too early, I'm putting it on record: in the coming chapters, AGI is a functional thing. The question of consciousness — and of whether a computational architecture can give rise to consciousness at all — we will take up seriously only in part three of the book.

Now for the main objection people usually throw at me at this point, the one that has to be dealt with here so it doesn't hang over the whole book.

"But AGI doesn't exist yet. Why compare yourself to something that doesn't exist?"

Because the cost of being wrong is asymmetric. And this is not a philosophical argument but a strictly practical one, drawn from the everyday logic of managing your own life.

If I compare myself with GPT-5, find where I'm better, and build my career and my picture of the world on that — and then ten years later an AGI appears against which my findings collapse — it means I built my life on a temporary head start. I was soothed by an illusion with no long-term value. By that point it will be too late to rebuild: the competencies I bet on are zeroed out, and I have less time to accumulate new ones than I had at the start. But if from the very beginning I ask myself "what will I have left in the face of genuinely general intelligence," then even if AGI is delayed or never comes at all, in the worst case I end up with a deeper understanding of how I work, a more honest picture of my own limits, and a more precise place in reality. This bet loses only if AGI never appears at all and I also get no benefit whatsoever from the thinking. In every other case, it wins.

This is not "caution" in the usual sense. Caution is about reducing risk when the options are symmetric. Here the stake is asymmetric: on one side of the scale, a short-term win in comfort, on the condition that the world stays the way it is now. On the other, a long-term win in orientation, under any scenario but one. Betting on "I'm stronger than AGI" is betting that the world is forbidden to change. I don't know a weaker bet in life. Getting smacked for thinking too early costs, at worst, a few years of uncomfortable thought. Getting smacked for thinking too late costs a career and costs scale.

And one more thing. Knowing the limits of your own advantage is intellectual hygiene — a form of it that has nothing to do with AGI as such. Any professional who can tell the difference between what they're genuinely strong at and what they're strong at merely because no one has gotten in their way yet lives more steadily than one who confuses the two. The AGI question is a special case of this general rule. It just pushes the rule to its limit: "imagine that an agent appears in your field who is objectively stronger than you on most parameters. What do you have left?" If you can answer honestly — you have your bearings in your own life. If not — you're living on faith that nothing will change. And it changes.

That is the answer to "why compare with AGI." Not because it's certain to arrive tomorrow, but because it's the only honest frame within which the question makes sense. All the other frames are, to one degree or another, about giving yourself permission not to think.

And now that AGI is defined and the definition doesn't slip, we can bring to it all the classic answers to "so what will humans have left." There are many. They're everywhere. They're repeated by the same people who, back in chapter one, suggested becoming a plumber.

The trouble is, those answers were built in an era when a human had only one rival — another human. They were honed for that rival. Holding them up against AGI — and seeing what survives and what crumbles — is its own unpleasant labor, one that takes up more than a page of this book. I'll take each of them in turn. And I'll try not to gloat.

