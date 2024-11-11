using Microsoft.EntityFrameworkCore;

public class SupplierService : ISupplierService
{

    private readonly DataContext _context;

    public SupplierService(DataContext context){
        _context = context;
    }

    public async Task<IEnumerable<Supplier>?> GetSuppliers(){
        return await _context.Suppliers.ToListAsync();
    }


    public async Task<Supplier?> GetSupplier(int SupplierId){
        return await _context.Suppliers.FindAsync(SupplierId);
    }


    public async Task<IEnumerable<Item>?> GetItems(int SupplierId){
        return await _context.Items.Where(item => item.SupplierId == SupplierId).ToListAsync();
    }


    public async Task<Supplier?> AddSupplier(Supplier supplier){
        supplier.CreatedAt = DateTime.Now;
        supplier.UpdatedAt = DateTime.Now;
        await _context.Suppliers.AddAsync(supplier);
        await _context.SaveChangesAsync();
        return await GetSupplier(supplier.Id);
    }


    public async Task<Supplier?> UpdateSupplier(int SupplierId, Supplier supplier){
        supplier.Id = SupplierId;
        supplier.UpdatedAt = DateTime.Now;
        _context.Suppliers.Update(supplier);
        await _context.SaveChangesAsync();
        return await GetSupplier(SupplierId);
    }


    public async Task DeleteSupplier(int SupplierId){
        Supplier? supplier = await _context.Suppliers.FindAsync(SupplierId);
        if(supplier == null) return;
        _context.Suppliers.Remove(supplier);
        await _context.SaveChangesAsync();
    }



}

public interface ISupplierService
{

    Task<IEnumerable<Supplier>?> GetSuppliers();
    Task<Supplier?> GetSupplier(int SupplierId);
    Task<IEnumerable<Item>?> GetItems(int SupplierId);
    Task<Supplier?> AddSupplier(Supplier supplier);
    Task<Supplier?> UpdateSupplier(int SupplierId, Supplier supplier);
    Task DeleteSupplier(int SupplierId);

}