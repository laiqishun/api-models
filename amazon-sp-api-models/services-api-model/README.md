---
title: Selling Partner API for Services
description: "With the Services API, you can build applications that help service providers get and modify their service orders and manage their resources."
---

# API List
- [getServiceJobByServiceJobId](operations/getServiceJobByServiceJobId.json) (GET /service/v1/serviceJobs/{serviceJobId})：Gets details of service job indicated by the provided `serviceJobID`.
- [cancelServiceJobByServiceJobId](operations/cancelServiceJobByServiceJobId.json) (PUT /service/v1/serviceJobs/{serviceJobId}/cancellations)：Cancels the service job indicated by the service job identifier specified.
- [completeServiceJobByServiceJobId](operations/completeServiceJobByServiceJobId.json) (PUT /service/v1/serviceJobs/{serviceJobId}/completions)：Completes the service job indicated by the service job identifier specified.
- [getServiceJobs](operations/getServiceJobs.json) (GET /service/v1/serviceJobs)：Gets service job details for the specified filter query.
- [addAppointmentForServiceJobByServiceJobId](operations/addAppointmentForServiceJobByServiceJobId.json) (POST /service/v1/serviceJobs/{serviceJobId}/appointments)：Adds an appointment to the service job indicated by the service job identifier specified.
- [rescheduleAppointmentForServiceJobByServiceJobId](operations/rescheduleAppointmentForServiceJobByServiceJobId.json) (POST /service/v1/serviceJobs/{serviceJobId}/appointments/{appointmentId})：Reschedules an appointment for the service job indicated by the service job identifier specified.
- [assignAppointmentResources](operations/assignAppointmentResources.json) (PUT /service/v1/serviceJobs/{serviceJobId}/appointments/{appointmentId}/resources)：Assigns new resource(s) or overwrite/update the existing one(s) to a service job appointment.
- [setAppointmentFulfillmentData](operations/setAppointmentFulfillmentData.json) (PUT /service/v1/serviceJobs/{serviceJobId}/appointments/{appointmentId}/fulfillment)：Updates the appointment fulfillment data related to a given `jobID` and `appointmentID`.
- [getRangeSlotCapacity](operations/getRangeSlotCapacity.json) (POST /service/v1/serviceResources/{resourceId}/capacity/range)：Provides capacity slots in a format similar to availability records.
- [getFixedSlotCapacity](operations/getFixedSlotCapacity.json) (POST /service/v1/serviceResources/{resourceId}/capacity/fixed)：Provides capacity in fixed-size slots.
- [updateSchedule](operations/updateSchedule.json) (PUT /service/v1/serviceResources/{resourceId}/schedules)：Update the schedule of the given resource.
- [createReservation](operations/createReservation.json) (POST /service/v1/reservation)：Create a reservation.
- [updateReservation](operations/updateReservation.json) (PUT /service/v1/reservation/{reservationId})：Update a reservation.
- [cancelReservation](operations/cancelReservation.json) (DELETE /service/v1/reservation/{reservationId})：Cancel a reservation.
- [getAppointmmentSlotsByJobId](operations/getAppointmmentSlotsByJobId.json) (GET /service/v1/serviceJobs/{serviceJobId}/appointmentSlots)：Gets appointment slots for the service associated with the service job id specified.
- [getAppointmentSlots](operations/getAppointmentSlots.json) (GET /service/v1/appointmentSlots)：Gets appointment slots as per the service context specified.
- [createServiceDocumentUploadDestination](operations/createServiceDocumentUploadDestination.json) (POST /service/v1/documents)：Creates an upload destination.
