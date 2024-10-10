import llm_mathjudger
import time

def timer(f, **kwargs):
    start = time.perf_counter()
    print(f(**kwargs))
    end = time.perf_counter()
    print(f"Time taken: {(end - start) * 1000} milliseconds")

problem = {"problem": "Compute\n\\[\\frac{1}{\\cos^2 10^\\circ} + \\frac{1}{\\sin^2 20^\\circ} + \\frac{1}{\\sin^2 40^\\circ}.\\]", "solution": "We can write\n\\begin{align*}\n\\frac{1}{\\cos^2 10^\\circ} &= \\frac{2}{1 + \\cos 20^\\circ} \\\\\n&= \\frac{2 (1 - \\cos 20^\\circ)}{(1 + \\cos 20^\\circ)(1 - \\cos 20^\\circ)} \\\\\n&= \\frac{2 (1 - \\cos 20^\\circ)}{1 - \\cos^2 20^\\circ} \\\\\n&= \\frac{2 - 2 \\cos 20^\\circ}{\\sin^2 20^\\circ},\n\\end{align*}so\n\\begin{align*}\n\\frac{1}{\\cos^2 10^\\circ} + \\frac{1}{\\sin^2 20^\\circ} + \\frac{1}{\\sin^2 40^\\circ} &= \\frac{2 - 2 \\cos 20^\\circ}{\\sin^2 20^\\circ} + \\frac{1}{\\sin^2 20^\\circ} + \\frac{1}{\\sin^2 40^\\circ} \\\\\n&= \\frac{3 - 2 \\cos 20^\\circ}{\\sin^2 20^\\circ} + \\frac{1}{\\sin^2 40^\\circ} \\\\\n&= \\frac{4 \\cos^2 20^\\circ (3 - 2 \\cos 20^\\circ)}{4 \\sin^2 20^\\circ \\cos^2 20^\\circ} + \\frac{1}{\\sin^2 40^\\circ} \\\\\n&= \\frac{12 \\cos^2 20^\\circ - 8 \\cos^3 20^\\circ}{\\sin^2 40^\\circ} + \\frac{1}{\\sin^2 40^\\circ} \\\\\n&= \\frac{12 \\cos^2 20^\\circ - 8 \\cos^3 20^\\circ + 1}{\\sin^2 40^\\circ}.\n\\end{align*}By the triple angle formula,\n\\begin{align*}\n\\frac{1}{2} &= \\cos 60^\\circ \\\\\n&= \\cos (3 \\cdot 20^\\circ) \\\\\n&= 4 \\cos^3 20^\\circ - 3 \\cos 20^\\circ,\n\\end{align*}which means $8 \\cos^3 20^\\circ = 6 \\cos 20^\\circ + 1.$  Hence,\n\\begin{align*}\n\\frac{12 \\cos^2 20^\\circ - 8 \\cos^3 20^\\circ + 1}{\\sin^2 40^\\circ} &= \\frac{12 \\cos^2 20^\\circ - 6 \\cos 20^\\circ}{\\sin^2 40^\\circ} \\\\\n&= \\frac{12 \\cos^2 20^\\circ - 6 \\cos 20^\\circ}{4 \\sin^2 20^\\circ \\cos^2 20^\\circ} \\\\\n&= \\frac{12 \\cos 20^\\circ - 6}{4 \\sin^2 20^\\circ \\cos 20^\\circ} \\\\\n&= \\frac{12 \\cos 20^\\circ - 6}{4 (1 - \\cos^2 20^\\circ) \\cos 20^\\circ} \\\\\n&= \\frac{12 \\cos 20^\\circ - 6}{4 \\cos 20^\\circ - 4 \\cos^3 20^\\circ} \\\\\n&= \\frac{12 \\cos 20^\\circ - 6}{4 \\cos 20^\\circ - 3 \\cos 20^\\circ - \\frac{1}{2}} \\\\\n&= \\frac{12 \\cos 20^\\circ - 6}{\\cos 20^\\circ - \\frac{1}{2}} \\\\\n&= \\boxed{12}.\n\\end{align*}", "answer": "12", "subject": "Precalculus", "level": 4, "unique_id": "test/precalculus/989.json"}

timer(
    llm_mathjudger.check,
    data_name="math_oai",
    target=problem,
    pred="Therefore, the answer is approximately 12.",
    execute=False,
    vis=True
)

timer(
    llm_mathjudger.check,
    data_name="math_oai",
    target=problem,
    pred="Therefore, the answer is 12.",
    execute=False,
    vis=True
)

timer(
    llm_mathjudger.check,
    data_name="math_oai",
    target=problem,
    pred="Therefore, the answer is 3 * 4.",
    execute=True,
    vis=True
)

timer(
    llm_mathjudger.check,
    data_name="math_oai",
    target=problem,
    pred="Therefore, the answer is approximately \\boxed{12}.",
    execute=False,
    vis=True
)

print(llm_mathjudger.extract("math_oai", "Therefore, the answer is approximately \\boxed{12}."))
print(llm_mathjudger.extract("math_oai", "Therefore, the answer is approximately 12."))
print(llm_mathjudger.extract("math_oai", "Therefore, the answer is 3 * 4."))
