from flask import Flask, render_template, request
app = Flask(__name__)

#-------------------------------lista--------------------------------------


listado_productos = [
    dict(
        id = '1',
        products = "Gabinete",
        category = "Nuevo"
    ),
    
]


#----------------------------------rutas-------------------------------------

@app.route('/') #app es la instancia - route el metodo, '/' es el disparador
def index():
    return render_template(
        'index.html', 
    )


@app.route('/productos', methods = ['GET'])
def productos():
    productos = listado_productos
    return render_template(
        'productos.html', 
        productos = productos
        
    )


@app.route('/productos/add', methods = ['POST', 'GET'])  #cuando explicito un metodo tengo que hacer todas las rutas
def agrega_producto():
    if request.method == 'POST':
        id = request.form['id']
        products = request.form['producto']
        category = request.form['categoria']
        
        nuevo_producto = dict(
            id = id,
            products = products,
            category = category,
        )
        
        listado_productos.append(nuevo_producto)
        print(nuevo_producto)
    return render_template('add_producto.html')





