[Transition] The most technical question in the docs is why SVG sits at the center of the system.

The argument is practical rather than ideological. DrawingML is too verbose to author reliably, HTML and CSS speak the wrong layout language, WMF and EMF are not useful AI targets, and image-only SVG throws away editability. SVG wins because it shares the same absolute-coordinate mindset as slide graphics while remaining readable and transformable.

Key points: (1) SVG is chosen by elimination (2) It matches the slide canvas worldview (3) It remains inspectable before export  
Duration: 1.5 minutes