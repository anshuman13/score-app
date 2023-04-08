import { MessageTextType } from '../types/MessageTextType';

export const AlertMessage = (props: MessageTextType) => {
  if (props.type === 'Success') {
    return (
      <div
        className='flex items-center bg-[#FAF6FF] text-[#351B44] text-lg p-[16px] border border-solid border-[#741ada66] rounded-[10px]'
        role='alert'
      >
        <p>{props.messageText}</p>
      </div>
    );
  }
  if (props.type === 'Error') {
    return (
      <div
        className='flex items-center bg-[#FAF6FF] text-[#351B44] text-lg p-[16px] border border-solid border-red-400 rounded-[10px]'
        role='alert'
      >
        <p>{props.messageText}</p>
      </div>
    );
  }
  return <></>;
};
