from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

FLASHCARDS = [
    {"id": 1, "topic": "速さ・時間・距離",
     "formula_latex": r"v=\frac{d}{t},\quad d=vt,\quad t=\frac{d}{v}",
     "question": "あるランナーが分速120 mで7分間走った。移動距離 d は？",
     "answer": r"d=120\times 7=840\ \mathrm{m}", "hint": "d=vt を使う。"},
    {"id": 2, "topic": "平均速度",
     "formula_latex": r"\text{平均速度}=\frac{\text{総距離}}{\text{総時間}}",
     "question": "A→B 2 km を時速6 km、B→A 2 km を時速4 km。往復平均速度は？",
     "answer": r"\frac{4}{\frac{2}{6}+\frac{2}{4}}=\frac{24}{5}=4.8\ \mathrm{km/h}",
     "hint": "距離一定のときは単純平均ではない。"},
    {"id": 3, "topic": "出会い・追いつき",
     "formula_latex": r"t_{\text{出会い}}=\frac{d}{v_1+v_2},\quad t_{\text{追いつき}}=\frac{d}{|v_1-v_2|}",
     "question": "2000 m 離れた2人が90と110 m/分で互いに接近。出会う時刻 t は？",
     "answer": r"t=\frac{2000}{90+110}=10\ \mathrm{分}", "hint": r"和速度 v_1+v_2。"},
    {"id": 4, "topic": "割合",
     "formula_latex": r"\text{部分}=\text{全体}\times \text{割合},\quad 15\% = 0.15",
     "question": "15%引きで1700円。元値は？",
     "answer": r"\frac{1700}{0.85}=2000\ \mathrm{円}", "hint": r"値引後=全体×(1-0.15)。"},
    {"id": 5, "topic": "平均（算術平均）",
     "formula_latex": r"\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i",
     "question": "3人の平均72点。2人は68点・75点。残り1人は？",
     "answer": r"3\times 72-(68+75)=73\ \mathrm{点}", "hint": "合計=平均×人数。"},
    {"id": 6, "topic": "仕事算（和で足す）",
     "formula_latex": r"\text{同時作業量}=\frac{1}{a}+\frac{1}{b}",
     "question": "A単独4日、B単独6日。2人で何日？",
     "answer": r"\left(\frac{1}{4}+\frac{1}{6}\right)^{-1}=\frac{12}{5}=2.4\ \mathrm{日}",
     "hint": "日数の逆数（率）を足す。"},
    {"id": 7, "topic": "比と割合",
     "formula_latex": r"a:b=\frac{a}{b}",
     "question": "比 2:3 の合計が300。各値は？",
     "answer": r"2+3=5\Rightarrow 1\text{単位}=60\Rightarrow 120,\ 180",
     "hint": "和を単位に割り当てる。"},
    {"id": 8, "topic": "組合せ",
     "formula_latex": r"{}_n\mathrm{C}_r=\frac{n!}{r!(n-r)!}",
     "question": "5人から2人を選ぶ組合せは？",
     "answer": r"{}_5\mathrm{C}_2=10", "hint": "順不同の選び方。"},
    {"id": 9, "topic": "等差数列の和",
     "formula_latex": r"S_n=\frac{n(a_1+a_n)}{2}",
     "question": "初項3、公差2、項数10 の和は？",
     "answer": r"a_{10}=21,\ S_{10}=120", "hint": "初末項の平均×項数。"},
    {"id": 10, "topic": "速さ（時速と分速）",
     "formula_latex": r"\text{時速} = 60\times \text{分速}",
     "question": "分速150 m は時速何 km？",
     "answer": r"0.15\times 60=9\ \mathrm{km/h}", "hint": "1分→1時間へ換算。"},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/cards")
def api_cards():
    return jsonify({"cards": FLASHCARDS})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # 本番は Gunicorn（WSL/Linux）で起動。ローカル確認のみ開発サーバを使用。
    app.run(host="0.0.0.0", port=port, debug=False)
