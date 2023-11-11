// ***********************
// дата

const date = document.getElementById('date');
date.innerHTML = new Date().getFullYear();

// ***********************
// сжатие страницы (для меню)

const navToggle = document.querySelector(".nav-toggle");
const linksContainer = document.querySelector(".links-container");
const links = document.querySelector(".links");

navToggle.addEventListener("click", function() {
  // linksContainer.classList.toggle("show-links");
  const containerHeight = linksContainer.getBoundingClientRect().height; // возвращает DOMRectобъект, предоставляющий информацию о размере элемента и его положении относительно области просмотра .
  const linksHeight = links.getBoundingClientRect().height;

  if (containerHeight === 0) {
    linksContainer.style.height = `${linksHeight}px`;
  } else {
    linksContainer.style.height = 0;
  }
});

// ***********************
// закрепляется менюшка, меняются цвета

const navbar = document.getElementById('nav');
const toplink = document.querySelector('.top-link');

// изменяют классы HTML элементов navbar и toplink в зависимости от того, сколько пользователь прокрутил страницу
// "слушает", будет ли такое событие
// блоки отличаются в том, как они назначают обработчики событий

// window.addEventListener("scroll", function() {
//   const scrollHeight = window.pageYOffset;
//   const navHeight = navbar.getBoundingClientRect().height;
// // Здесь обработчик события задан непосредственно внутри addEventListener в виде анонимной функции.
// //Это означает, что когда событие scroll происходит, функция будут выполнена.

//   if (scrollHeight > navHeight) {
//     navbar.classList.add("fixed-nav");
//   } else {
//     navbar.classList.remove("fixed-nav");
//   }

// // ***********************
// // стрелка наверх

//   if (scrollHeight > 500) {
//     toplink.classList.add("show-link");
//   } else {
//     toplink.classList.remove("show-link");
//   }
// });

// блоки отличаются в том, как они назначают обработчики событий
// scroll() - предварительно определенная функция, которая вызывается при создании обработчика события

function scroll() {
  const scrollHeight = window.pageYOffset; // переменная хранит текущую вертикальную позицию прокрутки страницы
  const navHeight = navbar.getBoundingClientRect().height; // переменная хранит высоту элемента с идентификатором navbar на веб-странице

  // проверяет, если количество прокрученного контента больше высоты элемента navbar
  if (scrollHeight > navHeight) {
    // тогда к этому элементу применяется класс fixed-nav, который может менять его позиционирование и другиет стили
    navbar.classList.add("fixed-nav");
  } else { 
    // иначе, если прокрутка меньше высоты navbar, класс fixed-nav удаляется
    navbar.classList.remove("fixed-nav");
  }

// ***********************
// проверяет, если количество прокрученного контента больше 500 пикселей, тогда к элементу с идентификатором toplink добавляется класс show-link
  if (scrollHeight > 500) {
    toplink.classList.add("show-link");
  } else {
    toplink.classList.remove("show-link");
  }
}
window.addEventListener('scroll', scroll)
//  добавляет обработчик событий к объекту window

// API С ПОГОДОЙ

// 1 ВАРИАНТ (простой fetch-запрос)

// const weatherContainer = document.getElementById("weather-container");
// fetch('http://api.openweathermap.org/data/2.5/weather?id=491422&units=metric&appid=b9a699d1fd5917547eeea0341fed9a95')
//   .then(response => response.json())
//   .then(data => {
//     const temp = data.main.temp;
//     const weather = document.createElement("p");
//     weather.innerText = `Сейчас в Сочи: ${temp}°C`;
//     weatherContainer.append(weather);
//   })
//   .catch(error => console.log(error));


// 2 ВАРИАНТ
// определяем конструктор, который принимает 'apiKey'
// и сохраняет его в свойстве 'this.apiKey'
window.addEventListener('DOMContentLoaded', function() { // ф-ция обработчик
  class WeatherAPI {
    constructor(apiKey) {
      this.apiKey = apiKey;
    }
    // метод getWeather()
    // исп ключевое слово async и оператор await для выполнения асинхронных операций
    // fetch для отправки запроса и получения ответа

    async getWeather(cityId) {
      try {
        const response = await fetch(`http://api.openweathermap.org/data/2.5/weather?id=${cityId}&units=metric&appid=${this.apiKey}`);
        const data = await response.json();
        return data.main.temp;
      } catch (error) {
        console.log(error);
      }
    }
  }

  // при получении данных о погоде, создаем элемент `<p>` и устанавливаем его содержимое с помощью свойства `innerText`
  // созданный элемент добавляем в контейнер с помощью метода `append`
  
  const weatherContainer = document.querySelector('#weather-container');
  const weatherAPI = new WeatherAPI('b9a699d1fd5917547eeea0341fed9a95'); // создание нового экземпляра объекта WeatherAPI с ключом API, который будет использоваться для получения данных о погоде
  weatherAPI.getWeather(491422)
    .then(temp => {
      const weather = document.createElement("p");
      weather.innerText = `Сейчас в Сочи: ${temp}°C`;
      weatherContainer.append(weather);
    })
    .catch(error => console.log(error));
});

// На заметку
// web storm - IDE
//1. npm init - подклбчить бюлиотект для приведения к общему формату
//2. npm install