from app import app
from flask import render_template


@app.route('/')
@app.route('/restaurant', methods=['GET', 'POST'])
def Restaurant():
    #This page wil show restaurant.
    return render_template('restaurant.html', restaurants=restaurants)

@app.route('/restaurant/new', methods=['GET', 'POST'])
def newtable():
    # This page will be for making a new table.
    return render_template('newtable.html')

@app.route('/restaurant/<int:table_id>/edit/', methods=['GET', 'POST'])
def edittable(table_id):
    # This page will be for editing table
    return render_template('edittable.html')

@app.route('/restaurant/<int:table_id>/delete', methods=['GET', 'POST'])
def deletetable(table_id):
    # This page will be for deleting table
    return render_template('deletetable.html')

@app.route('/restaurant/<int:table_id>/')
@app.route('/restaurant/<int:table_id>/menu', methods=['GET', 'POST'])
def showMenu(restaurant_id):
    # This page is the menu for restaurant
    return render_template('menu.html')

@app.route('/restaurant/<int:table_id>/menu/new', methods=['GET', 'POST'])
def newMenuItem(table_id):
    # This page is for making a new menu item for restaurant
    return render_template('newMenuItem.html')

@app.route('/restaurant/<int:table_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenuItem(table_id, menu_id):
    # This page is for editing menu item"
    return render_template('editMenuItem.html')

@app.route('/restaurant/<int:table_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(table_id, menu_id):
    # This page is for deleting menu item %s
    return render_template('deleteMenuItem.html')