import pandas as pd


class Email:
    __dataset = None
    head = None
    columns = None

    def __init__(self, file):
        self.__dataset = pd.read_csv(file)
        self.head = self.__dataset.iloc[:5]
        self.columns = self.__dataset.columns

    def get_data(self):
        print('The Data set is: ')
        print(self.head[self.columns[2]][0])
        return self.head[self.columns[2]]

    # @staticmethod
    def email_features(self, content):
        features = {'Message-ID' : } # to store all tags and features
        for instance in content:
            instance = instance.split('\n')     # split data to get separate features
            message = ''
            # for feature in instance:
            #     if ':' in feature and 'Re:' in feature: # for reply messages add another feature by seeing RE in data
            #         feature = feature.split(':')
            #         if feature[0] not in features.keys():
            #             features[feature[0]] = [feature[1::]]
            #         else:
            #             features[feature[0]].append(feature[1::])
            #     elif ':' in feature:
            #         feature = feature.split(':')
            #         if feature[0] not in features.keys():
            #             features[feature[0]] = [feature[1]]
            #         else:
            #             features[feature[0]].append(feature[1])
            #     else:
            #         message += feature+'\n'
            features['body'].append(message)
        features = pd.DataFrame.from_dict(features)
        self.__dataset = pd.concat([self.__dataset, features], axis=1)
        return self.__dataset


if __name__ == "__main__":
    print('test run 2')
    enron = Email('small_emails.csv')
    mail_1 = enron.get_data()
    enron.email_features(mail_1)

    print(enron.email_features(mail_1))
    print('test run complete')
