# slide_01_cover

This deck compresses the four key documentation files into a single story about what PPT Master is, how it works, and what it demands from the user. The central thread is not just AI slide generation. It is the ability to produce a PowerPoint file that remains editable and usable after export.

Key points: (1) This is a documentation synthesis deck (2) The story covers product, architecture, and setup (3) Editability is the anchor idea  
Duration: 1 minute

---

# slide_02_core_claim

[Transition] With the scope set, the first question is what PPT Master is actually trying to optimize for.

The answer is unusually concrete: not pretty screenshots, but a real slide file. The docs make the standard explicit: if the result cannot be opened and edited like a normal PowerPoint deck, then the workflow has missed the point. That framing shapes every downstream engineering decision.

Key points: (1) Native editability is the core differentiator (2) Engineering choices follow that principle (3) The deck is treated as a working file  
Duration: 1 minute

---

# slide_03_market_tradeoffs

[Transition] Once that standard is clear, the next step is to understand what other AI slide approaches get wrong.

The docs reject three familiar paths. Image embedding looks polished but destroys editability, HTML and CSS do not map cleanly to slide geometry, and direct python-pptx generation stays editable but usually lacks visual richness. PPT Master positions itself as the fourth path by using SVG as the drafting layer and DrawingML as the delivery layer.

Key points: (1) Three common approaches have hard limitations (2) PPT Master is a deliberate alternative (3) The product is framed through trade-offs, not hype  
Duration: 1.5 minutes

---

# slide_04_value_grid

[Transition] That positioning becomes easier to believe when the product values stay consistent across all docs.

Four themes repeat everywhere: real PowerPoint output, predictable cost, local-first data handling, and no lock-in on editors or models. These are not decorative claims. They explain why the project is open source, why the workflow runs locally, and why the docs spend so much time on practical setup and export behavior.

Key points: (1) Editability, cost, privacy, and openness define the product (2) The values are operational, not just branding (3) The docs are coherent across topics  
Duration: 1 minute

---

# slide_05_system_architecture

[Transition] After the product promise, the architecture tells us how the promise is delivered.

The full workflow is intentionally serial. Content gets normalized first, then the strategist plans the deck, then the executor generates SVG and notes, then post-processing cleans everything up before export. The docs are explicit that this serialization protects cross-slide consistency and reduces context drift.

Key points: (1) The workflow is stage-based and serial (2) Each stage hands off to the next (3) Consistency is prioritized over raw speed  
Duration: 1.5 minutes

---

# slide_06_three_stages

[Transition] We can simplify that architecture further into three conceptual stages.

Stage one is understanding and planning, stage two is visual generation, and stage three is engineering conversion. That separation is important because it clarifies the role of AI: first to interpret content, then to design with SVG, and finally to let deterministic scripts translate the draft into a real slide artifact.

Key points: (1) Understand (2) Generate (3) Convert  
Duration: 1 minute

---

# slide_07_why_svg

[Transition] The most technical question in the docs is why SVG sits at the center of the system.

The argument is practical rather than ideological. DrawingML is too verbose to author reliably, HTML and CSS speak the wrong layout language, WMF and EMF are not useful AI targets, and image-only SVG throws away editability. SVG wins because it shares the same absolute-coordinate mindset as slide graphics while remaining readable and transformable.

Key points: (1) SVG is chosen by elimination (2) It matches the slide canvas worldview (3) It remains inspectable before export  
Duration: 1.5 minutes

---

# slide_08_design_philosophy

[Transition] Even with the right architecture, the docs are careful not to over-promise the final quality.

The generated deck is described as a design draft, not a finished masterpiece. The workflow aims to remove most of the blank-page labor, but the user is still expected to review, refine, and finish the final mile. That honesty is one of the strongest parts of the documentation because it sets the right quality expectations upfront.

Key points: (1) AI is the designer, not the finisher (2) Human judgment stays central (3) The product is honest about its limits  
Duration: 1 minute

---

# slide_09_faq_snapshot

[Transition] The FAQ then translates those high-level ideas into the practical questions users actually ask.

The first cluster is basic operating scope: what formats can be read, what formats can be exported, what happens to charts, and whether the output is really editable. The answers are broad on input, explicit on output, and careful about chart limitations. The FAQ reads like a boundary-setting document as much as a help page.

Key points: (1) Input coverage is broad (2) Export behavior is explicit (3) Charts are visual shapes, not spreadsheet objects  
Duration: 1 minute

---

# slide_10_quality_expectations

[Transition] The next FAQ cluster is about quality, model choice, and what happens when a slide is not quite right.

The docs strongly favor Claude for layout-heavy generation, while admitting that other models may produce more overflow and coordinate errors. They also normalize an iterative review loop: inspect a page, describe the defect, regenerate or fix that page, and then polish inside PowerPoint. In other words, quality comes from model choice plus editorial process.

Key points: (1) Model quality matters (2) Review and repair are expected (3) The output is a strong starting point, not an automatic final answer  
Duration: 1 minute

---

# slide_11_windows_setup

[Transition] Once expectations are clear, the setup guide shows the shortest path to getting the workflow running on Windows.

The logic is simple: install Python correctly, get the project onto the machine, install dependencies, and verify the runtime before trying a larger deck. The repeated emphasis on PATH is not accidental. The guide treats environment correctness as the main gating factor for success.

Key points: (1) Python plus PATH is the first checkpoint (2) Dependencies and imports come next (3) A tiny sample deck proves the chain works  
Duration: 1 minute

---

# slide_12_troubleshooting

[Transition] The troubleshooting section reinforces the same lesson from a different angle.

Most failures are not presentation-design problems yet. They are environment problems: the wrong interpreter, the wrong pip target, blocked scripts, or missing modules. The right debugging order is to stabilize the machine first, then test imports, then run a minimal example, and only after that start debugging slide generation itself.

Key points: (1) Fix the environment before the slides (2) Use a structured debugging sequence (3) Edge-case tools are optional fallbacks  
Duration: 1 minute

---

# slide_13_closing_fit

[Transition] That brings us to the cleanest possible closing statement about who this workflow is for.

PPT Master is not the easiest or fastest slide tool. It is the tool for users who care more about editable, controllable output than instant browser convenience. If the audience values native PowerPoint behavior, local execution, predictable cost, and an open workflow, the docs argue that this is the right trade to make.

Key points: (1) Best for serious editable-output use cases (2) Not ideal for zero-setup browser workflows (3) The product is optimized for control, not ease alone  
Duration: 1 minute
