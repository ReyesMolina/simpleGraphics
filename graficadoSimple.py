from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':

    output_file('Graficado_simple.html')
    fig = figure()
    type(fig)
    
    total_vals = int(input('Cuantos valores quieres graficar?: '))
    x_val = list(range(total_vals))
    y_val = []

    for x in x_val:
        val = int(input(f'Valor Y para {x}'))
        y_val.append(val)

    fig.line(x_val, y_val, line_width=2)
    show(fig)

