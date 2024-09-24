import llm_mathjudger

data = {"problem": "Convert the point $(0,3)$ in rectangular coordinates to polar coordinates.  Enter your answer in the form $(r,\\theta),$ where $r > 0$ and $0 \\le \\theta < 2 \\pi.$", "solution": "We have that $r = \\sqrt{0^2 + 3^2} = 3.$  Also, if we draw the line connecting the origin and $(0,3),$ this line makes an angle of $\\frac{\\pi}{2}$ with the positive $x$-axis.\n\n[asy]\nunitsize(0.8 cm);\n\ndraw((-0.5,0)--(3.5,0));\ndraw((0,-0.5)--(0,3.5));\ndraw(arc((0,0),3,0,90),red,Arrow(6));\n\ndot((0,3), red);\nlabel(\"$(0,3)$\", (0,3), W);\ndot((3,0), red);\n[/asy]\n\nTherefore, the polar coordinates are $\\boxed{\\left( 3, \\frac{\\pi}{2} \\right)}.$", "answer": "\\left( 3, \\frac{\\pi}{2} \\right)", "subject": "Precalculus", "level": 2, "unique_id": "test/precalculus/807.json"}

print(llm_mathjudger.check(
    prompt_type="cot",
    data_name="math_oai",
    target=data,
    pred="We can get 4. So the final answer is \\left( 2 + 1, \\frac{\\pi}{4} + \\frac{\\pi}{4} \\right)."
))
