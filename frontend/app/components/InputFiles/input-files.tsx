import { zodResolver } from "@hookform/resolvers/zod";
import { Paperclip, UploadCloud } from "lucide-react";
import { useState } from "react";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { Form, FormControl, FormField, FormItem, FormMessage } from "~/components/ui/form";
import { Input } from "~/components/ui/input";

const formSchema = z.object({
  file: z.array(z.instanceof(File)).nonempty("Please select a file"),
});

export default function InputFile({ name }: { name: string }) {
  const [fileName, setFileName] = useState("No image selected");
  const [preview, setPreview] = useState<string | null>(null);
  const [uploading, setUploading] = useState(false);
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
  });

  const onSubmit = async (data: z.infer<typeof formSchema>) => {
    if (!data.file[0]) return;

    setUploading(true);
    const formData = new FormData();
    formData.append("faces", data.file[0]);

    try {
      const response = await fetch("/identifying/upload", {
        method: "POST",
        body: formData,
      });
      if (!response.ok) throw new Error("Upload failed");
      console.log("File uploaded successfully");
    } catch (error) {
      console.error(error);
    } finally {
      setUploading(false);
    }
  };

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-2">
        <FormField
          control={form.control}
          name="file"
          render={({ field: { onChange, ref } }) => (
            <FormItem>
              <FormControl>
                <div className="relative">
                  <label className="flex items-center gap-x-2 bg-gray-100 hover:bg-gray-200 px-2 py-2 border border-gray-300 rounded text-gray-700 transition-colors cursor-pointer">
                    <Paperclip size={20} />
                    <span className="font-medium text-sm">Choose an image</span>
                    <Input
                      type="file"
                      name={name}
                      ref={ref}
                      accept="image/*"
                      onChange={(e) => {
                        const file = e.target.files?.[0];
                        if (file) {
                          onChange(Array.from(e.target.files || []));
                          setFileName(file.name);
                          setPreview(URL.createObjectURL(file));
                          form.handleSubmit(onSubmit)();
                        }
                      }}
                      className="absolute inset-0 opacity-0 w-full h-full cursor-pointer"
                    />
                  </label>
                  <span className="text-gray-500 text-sm">{fileName}</span>
                </div>
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        {preview && (
          <div className="mt-2">
            <img src={preview} alt="Preview" className="shadow rounded-md w-20 h-20 object-cover" />
          </div>
        )}
        {uploading && (
          <div className="flex items-center gap-2 text-blue-500">
            <UploadCloud />
            Uploading...
          </div>
        )}
      </form>
    </Form>
  );
}
