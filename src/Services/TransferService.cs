using Microsoft.EntityFrameworkCore;
using ProjectC.Models;

public class TransferService : ITransferService
{
    private readonly DataContext _context;

    public TransferService(DataContext context)
    {
        _context = context;
    }

    public async Task<IEnumerable<Transfer>?> GetTransfers()
    {
        return await _context.Transfers.ToListAsync();
    }

    public async Task<Transfer?> GetTransfer(int transferId)
    {
        return await _context.Transfers.FindAsync(transferId);
    }

    public async Task<Transfer?> AddTransfer(Transfer transfer)
    {
        transfer.CreatedAt = DateTime.Now;
        transfer.UpdatedAt = DateTime.Now;
        await _context.Transfers.AddAsync(transfer);
        await _context.SaveChangesAsync();
        return await GetTransfer(transfer.Id);
    }

    public async Task UpdateTransfer(int transferId, Transfer transfer)
    {
        transfer.Id = transferId;
        transfer.UpdatedAt = DateTime.Now;
        _context.Transfers.Update(transfer);
        await _context.SaveChangesAsync();
    }

    public async Task DeleteTransfer(int transferId)
    {
        Transfer? transfer = await _context.Transfers.FindAsync(transferId);
        if (transfer == null) return;
        _context.Transfers.Remove(transfer);
        await _context.SaveChangesAsync();
    }
}

public interface ITransferService
{
    Task<IEnumerable<Transfer>?> GetTransfers();
    Task<Transfer?> GetTransfer(int transferId);
    Task<Transfer?> AddTransfer(Transfer transfer);
    Task UpdateTransfer(int transferId, Transfer transfer);
    Task DeleteTransfer(int transferId);
}