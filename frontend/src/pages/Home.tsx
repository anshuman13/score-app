import React, { Fragment, useState } from 'react';
import { FormInput } from '../components/form/FormInput';
import { Button } from '../shared/Button';
import { AlertMessage } from '../shared/AlertMessage';
import { NewScoreType } from '../types/NewScore/NewScoreType';
import { fetchScore } from '../services/NewScoreService';
import { MessageType } from '../types/MessageTextType';

export const Home = () => {
  const intialScoreState = {
    bodyTemprature: '',
    heartRate: '',
    respiratoryRate: '',
  };
  const [newsScoreState, setNewsScoreState] =
    useState<NewScoreType>(intialScoreState);
  const [messageType, setMessageTypeState] = useState<MessageType>('Error');
  const [score, setScore] = useState<number>();
  const [errorMessage, setErrorMessage] = useState<string>();
  const [showAlert, setShowAlert] = useState<boolean>(false);
  const newsScoreFields: {
    id: string;
    name: keyof typeof newsScoreState;
    type: string;
    isRequired: boolean;
    header: string;
    subHeader: string;
    placeholder: string;
  }[] = [
    {
      id: 'body-temprature',
      name: 'bodyTemprature',
      type: 'number',
      isRequired: true,
      header: 'Body temperature',
      subHeader: 'Degrees celcius',
      placeholder: '',
    },
    {
      id: 'heart-rate',
      name: 'heartRate',
      type: 'number',
      isRequired: true,
      header: 'Heart rate',
      subHeader: 'Beats per minute',
      placeholder: '',
    },
    {
      id: 'respiratory-rate',
      name: 'respiratoryRate',
      type: 'number',
      isRequired: true,
      header: 'Respiratory rate',
      subHeader: 'Breaths per minute',
      placeholder: '',
    },
  ];

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setNewsScoreState({ ...newsScoreState, [e.target.name]: e.target.value });
    setShowAlert(false);
  };

  const handleSubmit = async (e: any) => {
    try {
      const score = await fetchScore(newsScoreState);
      setScore(score.data.score);
      setShowAlert(true);
      setMessageTypeState('Success');
      resetForm();
    } catch (err: any) {
      if (err && err.data && err.data.measurements) {
        const key = parseInt(Object.keys(err.data.measurements)[0]);
        setErrorMessage(err.data.measurements[key].value[0]);
        setMessageTypeState('Error');
        setShowAlert(true);
      }
      throw new Error('Unable to fetech score.');
    }
  };

  const resetForm = () => {
    setNewsScoreState(intialScoreState);
  };

  return (
    <div className='flex flex-col items-center pt-[100px]'>
      <div className='flex flex-col gap-y-[40px]'>
        <h2 className='text-lg text-black font-semibold'>
          NEWS score calculator
        </h2>
        {newsScoreFields.map((newsScoreField) => (
          <FormInput
            key={newsScoreField.id}
            header={newsScoreField.header}
            subHeader={newsScoreField.subHeader}
            value={newsScoreState[newsScoreField.name]}
            id={newsScoreField.id}
            name={newsScoreField.name}
            type={newsScoreField.type}
            onChange={handleChange}
          />
        ))}
        <div className='flex gap-x-[20px]'>
          <Button
            description={'Calculate NEWS score'}
            className='btn-primary'
            onClick={handleSubmit}
          />
          <Button
            description={'Reset form'}
            className='btn-secondary'
            onClick={resetForm}
          />
        </div>
        {showAlert ? (
          messageType === 'Success' ? (
            <AlertMessage
              messageText={
                <Fragment>
                  News Score: <span className='font-bold'> {score} </span>
                </Fragment>
              }
              type={messageType}
            />
          ) : (
            <AlertMessage
              messageText={<Fragment> {errorMessage}</Fragment>}
              type={messageType}
            ></AlertMessage>
          )
        ) : (
          <></>
        )}
      </div>
    </div>
  );
};
