from pyscript import document

def show_summary(e):
    name = document.getElementById('Name').value
    address = document.getElementById('Address').value
    contact = document.getElementById('Contact').value

    item1 = document.getElementById('menu1')
    item2 = document.getElementById('menu2')
    item3 = document.getElementById('menu3')

    total = (float(item1.value) * item1.checked +
             float(item2.value) * item2.checked +
             float(item3.value) * item3.checked)

    summary = f"""
    Order for: {name}<br>
    Address: {address}<br>
    Contact number: {contact}<br>
    Total: ₱{total:.2f}
    """

    document.getElementById("summary").innerHTML = summary
