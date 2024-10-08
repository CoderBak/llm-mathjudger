# LLM-MathJudger

基于 [LLM-Math](https://github.com/CoderBak/llm-math) 简化的数学判别器. 该版本仅用于数学检查，因此不需要加载模型.

### Quick start

```bash
pip install llm-mathjudger
```

### Usage

1. `basic_check(A, B)`

   检查 A, B 两个**纯数学**表达式是否一致，返回 True / False.

2. `check(data_name, target, pred, execute, vis)`

   检查 pred 是否与 target 一致，返回 True / False. target 即为数据集的某一行.

   `execute=False` 表示是否采用 symbolic equal 和 math equal 进行等价判断.

   `vis=False` 表示是否输出 extracted answer.

### Example

```python
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
```

在 Mac 2020 M1 上的测试结果：

```text
Extracted answer: approximately12
False
Time taken: 11.696291999999996 milliseconds
Extracted answer: 12
True
Time taken: 1.7847079999999682 milliseconds
Extracted answer: 3*4
True
Time taken: 375.44279100000006 milliseconds
Extracted answer: 12
True
Time taken: 9.802499999999936 milliseconds
```
