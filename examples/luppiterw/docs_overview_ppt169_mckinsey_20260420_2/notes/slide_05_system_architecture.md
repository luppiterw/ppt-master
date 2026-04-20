[Transition] After the product promise, the architecture tells us how the promise is delivered.

The full workflow is intentionally serial. Content gets normalized first, then the strategist plans the deck, then the executor generates SVG and notes, then post-processing cleans everything up before export. The docs are explicit that this serialization protects cross-slide consistency and reduces context drift.

Key points: (1) The workflow is stage-based and serial (2) Each stage hands off to the next (3) Consistency is prioritized over raw speed  
Duration: 1.5 minutes