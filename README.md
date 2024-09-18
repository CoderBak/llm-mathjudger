# LLM-MathJudger

基于 [LLM-Math](https://github.com/CoderBak/llm-math) 简化的数学判别器. 该版本仅用于数学检查，因此不需要加载模型.

### Quick start

```bash
pip install llm-mathjudger
```

### Usage

1. `basic_check(A, B)`

   检查 A, B 两个**纯数学**表达式是否一致，返回 True / False.

2. `check(prompt_type, data_name, target, pred)`

   检查 pred 是否与 target 一致，返回 True / False. target 即为数据集的某一行.

- 支持的 prompt 类型: `tool-integrated`, `direct`, `cot`, `pal`, `self-instruct`, `self-instruct-boxed`, `tora`, `wizard_zs`, `platypus_fs`, `deepseek-math`, `kpmath`.

- 支持的数据集: `gsm8k`, `math`, `svamp`, `asdiv`, `mawps`, `tabmwp`, `mathqa`, `mmlu_stem`, `sat_math`.

### Example

```python
import llm_mathjudger

print(llm_mathjudger.basic_check('(0.6,3.6667]', '(\\frac{3}{5},\\frac{8}{3} + 1]'))
print(llm_mathjudger.check(
    prompt_type="cot",
    data_name="gsm8k",
    target={"question":"Kalinda is working on a 360 piece puzzle with her mom. Kalinda can normally add 4 pieces per minute. Her mom can typically place half as many pieces per minute as Kalinda.  How many hours will it take them to complete this puzzle?","answer":"Her mom places 2 pieces per minute because 4 \/ 2 = <<4\/2=2>>2\nOn average they get in 6 pieces per minute because 4 + 2 = <<4+2=6>>6\nIt will take 60 minutes to complete the puzzle because 360 \/ 6 = <<360\/6=60>>60\nIt will take one hour because 60 \/ 60 = <<60\/60=1>>1\n#### 1","idx":228},
    pred="Kalinda can add 4 pieces per minute. Her mom can add half as many pieces per minute as Kalinda. So her mom can add 2 pieces per minute. 360 pieces divided by 4 is 90. 90 divided by 2 is 45. 45 minutes is 1 hour. The answer is 1 hour."
))
```

### Note

该版本为了提高速度采用了激进的修改，还未经严格测试，请谨慎使用.
