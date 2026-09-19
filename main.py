from pyscript import document, display

def calculate_order(e):
    document.getElementById("receipt-body").innerHTML = "" # Resets the previous contents in the receipt

    # Get menu checkbox items from HTML
    plain = document.getElementById("item-plain")
    bacon = document.getElementById("item-bacon-egg")
    everything = document.getElementById("item-everything")
    french = document.getElementById("item-french-toast")
    cinnamon = document.getElementById("item-cinnamon")
    cold_brew = document.getElementById("item-cold-brew")

    subtotal = (
        # Calculate subtotal when we multiply the prices to its status (True or False)
        (float(plain.value) * plain.checked) +
        (float(bacon.value) * bacon.checked) +
        (float(everything.value) * everything.checked) +
        (float(french.value) * french.checked) +
        (float(cinnamon.value) * cinnamon.checked) +
        (float(cold_brew.value) * cold_brew.checked)
    )

    vat = subtotal * 0.12 # Gets 12% of subtotal to get VAT
    total = subtotal + vat # Total is measured by the sum of subtotal and the VAT

    display(f'subtotal: {subtotal} PhP', target="receipt-body")
    display(f'tax: {vat} PhP', target="receipt-body")
    display(f'total: {total} PhP', target="receipt-body")


# SKU Generator

def generate_sku(e):
    # Clear previous output inside the result box
    document.getElementById("sku-result").innerHTML = ""
    
    # Get values from inputs
    category = document.getElementById("category-input").value
    product = document.getElementById("product-input").value
    quantity = document.getElementById("qty-input").value
    
    # Combine inputs into formatted SKU
    sku = f"{category}-{product.upper()}-{quantity}"
    
    # Display inside the output container
    display(f"SKU: {sku}", target="sku-result")