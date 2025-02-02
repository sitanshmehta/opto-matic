from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# 现有的按钮标签数据 index of dropdown choice btn1 is same btn2 is better
BUTTON_LABELS = {
    'English': {'btn1': 'same', 'btn2': 'better'},
    '中文 (简体)': {'btn1': '相同', 'btn2': '更好'},
    'Español': {'btn1': 'mismo', 'btn2': 'mejor'},
    'Français': {'btn1': 'même', 'btn2': 'meilleur'},
    'Deutsch': {'btn1': 'gleich', 'btn2': 'besser'},
    '日本語': {'btn1': '同じ', 'btn2': 'より良い'},
    'Português': {'btn1': 'mesmo', 'btn2': 'melhor'},
    '한국어': {'btn1': '같은', 'btn2': '더 나은'},
    'Русский': {'btn1': 'тот же', 'btn2': 'лучше'},
    'العربية': {'btn1': 'نفس', 'btn2': 'أفضل'}
}

# API 路由 API connect
@app.route('/api/get_button_labels', methods=['GET'])
def get_button_labels():
    lang = request.args.get('lang', 'en')  
    """
    This line is get language from the choice if not choose default is English
    """
    labels = BUTTON_LABELS.get(lang, BUTTON_LABELS['English'])
    """
    Assign the exactly luanguage to the button
    """
    return jsonify(labels)
    """
    use unique form to display the button give it back to front
    """

# 新增主页路由 home API
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)