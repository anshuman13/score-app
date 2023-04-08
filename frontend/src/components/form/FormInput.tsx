import React from 'react';

type IFormInputProps = {
  header: string;
  subHeader: string;
  id: string;
  name: string;
  type: string;
  value: any;
  onChange: any;
};

export const FormInput = (props: IFormInputProps) => {
  return (
    <div className='flex flex-col gap-y-[12px]'>
      <form action=''>
        <div className='flex flex-col'>
          <span className='font-base font-semibold'>{props.header}</span>
          <span className='font-sm'>{props.subHeader}</span>
        </div>
        <input
          className='peer bg-[#FAF6FF] lg:min-w-[404px] lg:min-h-[41px] px-[10px] pl-[12px] pr-[24px]'
          id={props.id}
          name={props.name}
          value={props.value}
          type={props.type}
          onChange={props.onChange}
        />
      </form>
    </div>
  );
};
