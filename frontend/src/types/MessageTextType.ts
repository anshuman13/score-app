import { ReactElement } from 'react';

export type MessageType = 'Success' | 'Error';

export type MessageTextType = {
  messageText: ReactElement;
  type: MessageType;
};
