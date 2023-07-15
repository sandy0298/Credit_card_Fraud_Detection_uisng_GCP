CREATE OR REPLACE MODEL
transaction.credit_transaction_prediction
OPTIONS(model_type='BOOSTED_TREE_CLASSIFIER', INPUT_LABEL_COLS = ["isfraud"], MODEL_REGISTRY = 'VERTEX_AI',
VERTEX_AI_MODEL_ID='credit_card_bqml'
)
AS
SELECT
type,id,amount, oldbalanceOrig, newbalanceOrig, oldbalanceDest, newbalanceDest, isFraud,country,senders_name,receiver_bank,sender_bank,receiver_name,time_of_transaction
FROM transaction.fraud_data_model