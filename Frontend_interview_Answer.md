# Frontend Interview Answer

## [Javascript](https://github.com/sudheerj/javascript-interview-questions)

- Q. Explain **event delegation**.
- Q. What are **primitive data types**?

A primitive data type is data that has a primitive value (which has no properties or methods).
There are 7 primitive data types in javascript.

- `string`
- `number`
- `boolean`
- `null`
- `undefined`
- `bigint`
- `symbol`

- Q. What are the major features of primitive data types?

- 원시 타입은 불변성(immutable)을 갖고있다.
- 원시타입을 제외한 나머지는 참조 타입이다.
  - Primitive Type : 데이터의 실제 값 할당
  - Reference Type : 데이터의 위치 값만 할당

자바스크립트에서 원시 타입을 제외한 나머지는 참조타입(객체(Object))이라 할 수 있다. 배열과 객체, 그리고 함수가 대표적이며, 원시타입과 가장 큰 차이점은 변수의 크기가 동적으로 변한다는 것이다. 이러한 특징 때문에 Object의 데이터 자체는 별도의 메모리 공간(heap)에 저장되며, 변수에 할당 시 데이터에 대한 주소 ( 힙(Heap) 메모리의 주소값)가 저장되기 때문에 자바스크립트 엔진이 변수가 가지고 있는 메모리 주소를 이용해서 변수의 값에 접근하게 되는것이다.

## [React](https://github.com/sudheerj/reactjs-interview-questions#what-is-react)

- Q. What is React?

React is open-source javascript library maintained by Meta. React is used for building user interfaces, especially for single-page applications.

- Q. What are the major features of React?

The major features of React are:

- It uses **VirtualDOM** instead of RealDOM considering that updating RealDOM manipulations are expensive.
- Supports server-side rendering.
- Follows Unidirectional data flow or data binding.
- Uses reusable/composable User Interface components to develop the view.

- Q. What is JSX?

JSX stands for JavaScript XML.

https://velog.io/@sylagape1231/%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C-%EC%B7%A8%EC%A4%80%EC%83%9D%EC%9D%84-%EC%9C%84%ED%95%9C-%EA%B2%8C%EC%8B%9C%EA%B8%80%EC%9E%90%EB%A3%8C-%EB%AA%A8%EC%9D%8C
