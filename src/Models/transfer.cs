using System;

namespace ProjectC.Models
{
    public class Transfer
    {
        public string Reference { get; set; }
        public string TransferFrom { get; set; }
        public string TransferTo { get; set; }
        public string TransferStatus { get; set; }
        public DateTime CreatedAt { get; set; }
        public DateTime UpdatedAt { get; set; }

        public Transfer(string reference, string transferFrom, string transferTo, string transferStatus, DateTime createdAt, DateTime updatedAt)
        {
            Reference = reference;
            TransferFrom = transferFrom;
            TransferTo = transferTo;
            TransferStatus = transferStatus;
            CreatedAt = createdAt;
            UpdatedAt = updatedAt;
        }
    }

    public class TransferItem
    {
        public int ItemId { get; set; }
        public int Amount { get; set; }

        public TransferItem(int itemId, int amount)
        {
            ItemId = itemId;
            Amount = amount;
        }
    }
}