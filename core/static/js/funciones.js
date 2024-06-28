function mostrarProductos(){
    let url='http://localhost:3300/productos';
    fetch(url)
    .then(response => response.json())
    .then(data => mostrarArticulos(data))
    .catch(error => console.log(error))

    const mostrarArticulos=(data)=>{
        console.log(data)
        let texto=""
        for(var i=0;i<data.length;i++){
            texto+=`<tr>
                <td>${data[i].id}</td>
                <td>${data[i].nombre}</td>
                <td>${data[i].tipo}</td>
                <td>${data[i].picante}</td>
                </tr>`
        }
        document.getElementById('productos').innerHTML=texto;
    }


}


function buscarTipo(){
    let url='http://localhost:3300/productos';
    let tipo=document.getElementById('tipo').value;
    fetch(url)
    .then(response => response.json())
    .then(data => buscarProductos(data))
    .catch(error => console.log(error))

    const buscarProductos=(data)=>{
        console.log(data)
        let texto=""
        if (document.getElementById('tipo').selectedIndex==0){
            mostrarProductos();
        }
        else{

            for(var i=0;i<data.length;i++){
                if (tipo==data[i].tipo)
                {
                    texto+=`<tr>
                    <td>${data[i].id}</td>
                    <td>${data[i].nombre}</td>
                    <td>${data[i].tipo}</td>
                    <td>${data[i].picante}</td>
                    </tr>`
    
                }
            }
            document.getElementById('productos').innerHTML=texto;
        }
    }

}
function getRecetas(){
    let tipoComida = document.getElementById('tipoComida').value;
    let url = 'http://www.themealdb.com/api/json/v1/1/search.php?s=' + tipoComida;

    fetch(url)
    .then(response => response.json())
    .then(data => mostrarRecetas(data.meals))
    .catch(error => console.log(error))
}


function mostrarRecetas(meals){
    let texto = "";
    if(meals === null) {
        texto = "No se encontraron recetas para el tipo de comida ingresado.";
    } else {
        for(var i=0; i<meals.length; i++){
            texto += `<tr>
                        <td>${meals[i].strMeal}</td>
                        <td>${meals[i].strInstructions}</td>
                        <td><img src="${meals[i].strMealThumb}" alt="${meals[i].strMeal}"/></td>
                      </tr>`;
        }
    }
    document.getElementById('recetas').innerHTML = texto;
}