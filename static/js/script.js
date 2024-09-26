

// for catagori button

const catagory = document.getElementById('catagories')
const catagory_item = document.getElementById('catagoryItem')

catagory.addEventListener('click', async () => {
    let data = null
    try {
        const a = await fetch('http://127.0.0.1:8000/catagori/')
        data = await a.json()
    } catch (error) {
        console.log(error);
    }
    catagory_item.innerHTML = ''
    data.forEach(element => {
        catagory_item.innerHTML = catagory_item.innerHTML + `<a href="http://127.0.0.1:8000/catagory/${element.id}/" class="block px-4 py-2 text-gray-700 hover:bg-gray-100">${element.title}</a>`
    });

    catagory_item.classList.toggle('hidden');
    document.addEventListener('click', function (event) {
        if (!catagory.contains(event.target) && !catagory_item.contains(event.target)) {
            catagory_item.classList.add('hidden');
        }
    });
})

// for filter button////

const filter = document.getElementById('filter')
const filter_item = document.getElementById('filterForm')
const vendor_name = document.getElementById('vendor_name')

filter.addEventListener('click', async () => {

    try {
        const a = await fetch('http://127.0.0.1:8000/vendor-api/')
        let data = await a.json()

        const vendor = JSON.parse(data)


        console.log(vendor);

        vendor_name.innerHTML = ''
        vendor.forEach(element => {
            vendor_name.innerHTML = vendor_name.innerHTML + `<div class="flex items-center gap-1"><input type="checkbox" value="${element.pk}" name="item" id="">
            <div class="block px-4 py-2 text-gray-700 hover:bg-gray-100">${element.fields.title}</div></div>`
        });
    } catch (error) {
        console.log(error);
    }


    filter_item.classList.toggle('hidden');
    document.addEventListener('click', function (event) {
        if (!filter.contains(event.target) && !filter_item.contains(event.target)) {
            filter_item.classList.add('hidden');
        }
    });
})

//for prise Range

const inputRange = document.getElementById('input_range');
const startP = document.getElementById('start_P');
const endP = document.getElementById('end_P');

inputRange.addEventListener('input', function () {
    startP.textContent = `${inputRange.value}$`;
});

endP.addEventListener('click',()=>{
    inputRange.max = endP.value
    console.log(inputRange.getAttribute('max') );
    
})

