SELECT id, ROUND((julianday(closeDate) - julianday(openDate)) * 86400) AS timeOpen,
ROUND((julianday(waitingForThirdPartyDate) - julianday(waitingForCustomerDate)) * 86400) AS timeWaitingCustomer,
ROUND((julianday(resolvedDate) - julianday(waitingForThirdPartyDate)) * 86400) AS timeWaitedResponse,
ROUND((julianday(resolvedDate) - julianday(openDate)) * 86400) AS timeToResolved,
ROUND((julianday(waitingForCustomerDate) - julianday(openDate)) * 86400) AS timeToFirstResponse


FROM tickets;