import { AxiosResponse } from 'axios';
import { NewScoreType } from '../types/NewScore/NewScoreType';
import { ScoreApiMapping } from '../constants/ScoreMapping';
import { http } from '../utils/http';

type MeasurementType = {
  type: string;
  value: number;
};

type Payload = {
  measurements: MeasurementType[];
};

export const fetchScore = async (
  newsScore: NewScoreType
): Promise<AxiosResponse> => {
  const payload: Payload = { measurements: [] };

  for (const property in newsScore) {
    payload.measurements.push({
      type: ScoreApiMapping[property as keyof typeof ScoreApiMapping],
      value: parseFloat(newsScore[property as keyof object]),
    });
  }
  return await http.post('/calculate_news_score', payload);
};
