from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'GET':
        return render_template('index.html', display='0')

    try:
        action = request.form.get('action')
        display = request.form.get('display_value', '0')
        previous = request.form.get('previous_value', '')
        operator = request.form.get('operator_value', '')

        if action == 'C':
            return render_template('index.html', display='0')

        # Handle operators
        if action in ['add', 'subtract', 'multiply', 'divide']:
            if not operator:
                # First time an operator is pressed
                previous = display
                display = '0' # Reset for next number input
            elif operator and display != '0':
                # An operator is pressed sequentially when there is an operation pending
                n1 = float(previous)
                n2 = float(display)
                res = calculate(n1, n2, operator)
                if res == 'Error':
                    return render_template('index.html', display='Error')
                previous = format_result(res)
                display = '0' # Reset for next number
            
            operator = action
            
            
        elif action == 'equals':
            if operator and previous:
                n1 = float(previous)
                n2 = float(display)
                res = calculate(n1, n2, operator)
                
                if res == 'Error':
                     return render_template('index.html', display='Error')
                     
                display = format_result(res)
                # Reset state after equals
                previous = ''
                operator = ''
                
        # Numbers and decimal
        elif action in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
             # Prevent multiple decimals
            if action == '.' and '.' in display:
                pass 
            # Overwrite initial 0
            elif display == '0' and action != '.':
                display = action
            else:
                display += action
                
        # We need to maintain state variables
        return render_template('index.html', 
                               display=display, 
                               previous_value=previous, 
                               operator_value=operator)

    except Exception:
        return render_template('index.html', display='Error')


def calculate(n1, n2, operator):
    if operator == 'add':
        return n1 + n2
    elif operator == 'subtract':
        return n1 - n2
    elif operator == 'multiply':
        return n1 * n2
    elif operator == 'divide':
        if n2 == 0:
            return 'Error'
        return n1 / n2
    return 'Error'

def format_result(result):
     if result.is_integer():
         return str(int(result))
     return str(round(result, 6))

if __name__ == '__main__':
    app.run(debug=True)
