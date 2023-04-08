import React from 'react';

type IButtonText = {
  description: string;
  className: string;
  onClick: React.MouseEventHandler<HTMLButtonElement>;
};
export const Button = (props: IButtonText) => {
  return (
    <button className={props.className} onClick={props.onClick} type='submit'>
      {props.description}
    </button>
  );
};
