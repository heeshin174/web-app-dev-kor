import React, { useState } from "react";
import "./App.css";
import Inputfield from "./components/Inputfield";
import TodoList from "./components/TodoList";
import { Todo } from "./model";

// FC = Functional Component
const App: React.FC = () => {
  // useState = getter and setter
  const [todo, setTodo] = useState<string>("");
  // array of an interface
  const [todos, setTodos] = useState<Todo[]>([]);

  // add todo in todos
  // event type in typescript is React.FormEvent
  const handleAdd = (e: React.FormEvent) => {
    e.preventDefault(); // Not refresh the page

    if (todo) {
      // new todos = previous Todos (...todos) + new Todo
      // generate random id, isDone is false by default
      setTodos([...todos, { id: Date.now(), todo: todo, isDone: false }]);
      // empty the text when submit is performed.
      setTodo("");
    }
  };

  return (
    <div className="App">
      <span className="heading">Taskify</span>
      <Inputfield todo={todo} setTodo={setTodo} handleAdd={handleAdd} />
      <TodoList todos={todos} setTodos={setTodos} />
    </div>
  );
};

export default App;
