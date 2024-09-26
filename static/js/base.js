
// here change Domain Name
const domain_name = 'http://127.0.0.1:8000'

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function Cart_update() {
    let a = JSON.parse(localStorage.getItem('cartItem'))
    try {
        if (a.length > 0) {
            document.getElementById('Cart').innerHTML = `Cart(${a.length})`
        } else {
            document.getElementById('Cart').innerHTML = `Cart`
        }
        try {
            if (localStorage.getItem('OrderNo')) {
                const only_order = document.getElementById('onlyorder')
                const oid = localStorage.getItem('OrderNo')
                only_order.setAttribute('onclick', `Re_order('${oid}')`)
                only_order.innerHTML = 'Update'
            }
        } catch (error) {
            if (error instanceof TypeError) {
            } else {
                console.log('Error occurred:', error.message);
            }

        }
    } catch (error) {
        console.log(error);

    }
}
Cart_update()

function add(a) {
    try {
        const CartBTN = document.getElementById(a)
        CartBTN.onclick = null; // Prevent further clicks
        CartBTN.style.backgroundColor = '#CCCCCC'; // Change the background color to indicate it's disabled
        CartBTN.style.cursor = 'not-allowed';
        CartBTN.innerText = 'Added to Cart';

    } catch (error) {

    }

    let cartItem = [
        { 'item': a },
    ]
    if (localStorage.getItem('cartItem')) {
        let getItem = JSON.parse(localStorage.getItem('cartItem'))
        getItem.forEach(element => {
            if (element.item == a) {
                console.log('mached');
                return
            } else {
                cartItem.push(element)
            }
        });

    }

    localStorage.setItem('cartItem', JSON.stringify(cartItem))

    Cart_update()
}

function cart1() {
    try {
        let jsonData = JSON.parse(localStorage.getItem('cartItem'))

        const queryString = jsonData.map((obj) => `item=${encodeURIComponent(obj.item)}`).join('&');
        const url = `${domain_name}/cart?${queryString}`

        fetch(url)
            .then(response => response.text())
            .then(html => {
                document.getElementById('home').innerHTML = html
                Cart_update()
            })
            .catch(error => console.error('Error:', error));

    } catch (error) {
        document.getElementById('home').innerHTML = `
            <a class=" p-3 shadow-xl z-20 bg-white text-black rounded-lg" href="${domain_name}/">No Cart is hare . Go to shop</a>`
    }

}

function remove(a) {
    if (localStorage.getItem('cartItem')) {
        let getItem = JSON.parse(localStorage.getItem('cartItem'))
        let cartItem = getItem.filter(item => item.item !== a)
        localStorage.setItem('cartItem', JSON.stringify(cartItem))
        cart1()
        Cart_update()
    }
}

function Add_qty(a) {
    let qty = document.getElementById(a)
    qty.value = parseInt(qty.value) + 1
}

function Remove_qty(a) {
    let qty = document.getElementById(a)
    if (parseInt(qty.value) > 1) {
        qty.value = parseInt(qty.value) - 1
    }

}

async function Order(oid = null) {
    let url = ''
    let for_oder = []
    let a = document.querySelectorAll('.commonclass')
    a.forEach(element => {
        for_oder.push({ 'item': element.id, 'quantity': element.value })
    })

    if (oid != null) {
        url = `${domain_name}/uporder/${oid}/`
    } else {
        url = `${domain_name}/order/`
    }

    await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Assuming you have a function to get the CSRF token
        },
        body: JSON.stringify(for_oder)  // Convert the array to JSON string
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            if (data.bool) {
                alert('your order set successfully')
                localStorage.removeItem('cartItem')

                window.location.href = `${domain_name}/account/`;

                document.getElementById('home').innerHTML = `
                <a class=" p-3 shadow-xl z-20 bg-white text-black rounded-lg" href="${domain_name}/">No Cart is hare . Go to shop</a>`
            }
            else if (data.message == 'login-require'){
                window.location.href = `${domain_name}/user/sing-in/`
            }
            else if (data.message){
                alert(data.message)
            }
            else {
                alert('failed to make order')
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });

}

function sh_o_detail(oid) {
    const a = document.getElementById(oid)
    a.classList.toggle('hidden')
}

async function update_order(a) {
    let get_order = document.getElementById(a).getElementsByTagName('li')
    let url = `${domain_name}/cart?`
    Array.from(get_order).forEach((element) => {
        url += `item=${element.dataset.name}&`
        add(element.dataset.name)
    })
    url += `orderNo=${a}`
    await fetch(url)
        .then(response => response.text())
        .then(html => {
            document.getElementById('home').innerHTML = html
            localStorage.setItem('OrderNo', a)
            Cart_update()
        })
        .catch(error => console.error('Error:', error));

}

function Re_order(a) {
    Order(a);
    localStorage.removeItem('OrderNo')
}
async function cancleOrder(oid) {
    await fetch(`${domain_name}/cancle-order/${oid}/`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log('Order canceled successfully');
                document.getElementsByName(oid)[0].innerHTML = ''
            }
            else if(data.message){
                alert(data.message)
            }
             else {
                console.log('Failed to cancel the order');
            }
        })
        .catch((error) => {
            console.log("Error: ", error);
        });
}

function P_for_D(a) {
    window.location.href = `${domain_name}/bayling/${a}/`
}

function payment_method(a) {
    document.getElementById("fassdfadf").innerHTML = `
            <input name="payment_method" value="${a}" type="hidden">

           
            <div class="">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="phone">
                    Phone Number
                </label>
                <input requried name="phone" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="phone" type="number" placeholder="Enter your phone number">
            </div>

            <div class="">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="transaction-id">
                    Transaction ID
                </label>
                <input requried name="transaction_id" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="transaction-id" type="text" placeholder="Enter transaction ID">
            </div>

            <div class="">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="name">
                    Name
                </label>
                <input name="name" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="name" type="text" placeholder="Enter your name">
            </div>

            <div class="">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="date">
                    Date of your transaction ID
                </label>
                <input requried name="date" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="date" type="date">
            </div>
            <div class=" my-4 flex justify-center">
            <button class="p-2 rounded-md bg-purple-700 outline border border-black hover:cursor-pointer focus:bg-pink-500" type="submit">Get Delivery</button>
            </div>

             `
}
