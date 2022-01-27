import React, { useRef } from "react";
import "./styles.css";

interface Props {
  todo: string;
  setTodo: React.Dispatch<React.SetStateAction<string>>;
  handleAdd: (e: React.FormEvent) => void; // take event `e` and return void (nothing)
}

// setTodo function performs when text in inputbox is changed.
// handleAdd function performs when Go button is pressed.
const Inputfield: React.FC<Props> = ({ todo, setTodo, handleAdd }) => {
  // useRef is just like getElementbyId in normal JS.
  // type of input tag is HTMLInputElement
  const inputRef = useRef<HTMLInputElement>(null);
  // blur shifts the focus of inputbox when Go button is pressed.
  return (
    <form
      className="input"
      onSubmit={(e) => {
        handleAdd(e);
        inputRef.current?.blur();
      }}
    >
      <input
        type="input"
        className="input_box"
        placeholder="Enter a Task"
        value={todo}
        onChange={(e) => {
          setTodo(e.target.value);
        }}
      />
      <button className="input_submit" type="submit">
        Go
      </button>
    </form>
  );
};

export default Inputfield;
