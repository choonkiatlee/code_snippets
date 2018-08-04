import dash_js_executor
import dash
import dash_html_components as html

app = dash.Dash('')

app.scripts.config.serve_locally = True

app.layout = html.Div([
    dash_js_executor.ExampleComponent(
        id='input',
        src='''function(input) {
    console.log( input.a );
    return input.a;
}''',
        input={'a':'b'},
        text="Hello"    
    ),
    html.Div(id='output')
])



@app.callback(
    dash.dependencies.Output('output','children'),
    [dash.dependencies.Input('input','text')]
)
def echo(text_input):
    return text_input


if __name__ == '__main__':
    app.run_server(debug=False)
